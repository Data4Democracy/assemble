module MapUtils
using Plots


export create_data_dict

"""
a Map is a representation of a 2D scatter plot with labels and sizes
"""
type ScatterMap
	xlims::Tuple{Float64, Float64}
	ylims::Tuple{Float64, Float64}
	xys::Array{Tuple{Float64, Float64}, 1}
	colors::Array{ColorTypes.RGBA{Float64}, 1}
	sizes::Array{Float64, 1}
	labels::Array{Tuple{Float64, Float64, String}, 1}
end
ScatterMap(xlims::Tuple{Float64, Float64}, ylims::Tuple{Float64, Float64}) = ScatterMap(xlims, ylims, [], [], [], [])
function ScatterMap(xys::Array{Tuple{Float64, Float64}, 1},
		 color_scheme::Symbol,
		 community_labels::Array{Int64, 1},
		 sizes::Array{Float64, 1},
		 labels::Array{Tuple{Float64, Float64, String}, 1})
	
	# defining min and max for the xy data
	xs = [xy[1] for xy in xys]
	ys = [xy[2] for xy in xys]
	xlims = (minimum(xs), maximum(xs))
	ylims = (minimum(ys), maximum(ys))

	# mapping communities to colors, creating the color scheme
	n_labels = maximum(community_labels)
	cg = ColorGradient(color_scheme)
	color_vec = [cg[i] for i in linspace(0, 1, n_labels)]
	color_data = [color_vec[i] for i in community_labels]

	ScatterMap(xlims, ylims, xys, color_data, sizes, labels)
end

"""
A TiledMap is a dictionary of the quadtree of nested maps indexed by
(zoom_level, x_index, y_index)
"""
type TiledMap
	map_dict::Dict{Tuple{Int64, Int64, Int64}, ScatterMap}
	depth::Int64
end
TiledMap(depth::Int64) = TiledMap(Dict{Tuple{Int64, Int64, Int64}, ScatterMap}(), depth)
	
"""
This constructor takes in a number of zoom levels, a set of xlims and ylims,
an array of tuples representing the data, an array of colors representing 
some factor of the data, an array of sizes representing the data,
and a set of labels.
It returnes a TiledMap object, containing notably a dictionary indexed by
(zoom_level, xindex, yindex). 
"""
function TiledMap(zoom_levels::Int64,
			  imap::ScatterMap,
			  markersize::Array{Float64, 1})
	# initializing an empty tilemap
	tm = TiledMap(zoom_levels)

	marker_size_limit = quantile(markersize, [max(0,1-10*4^(zoom_level+1)/1000000) for zoom_level in 0:zoom_levels])
	
	# we first need to initialize the dictionary so we can push to any tile. 
	# we also calculate the boundaries for each tile in this
	# fist loop

	for zoom_level in 1:zoom_levels
		nb_subs = 2^(zoom_level - 1)
		delta_x = (imap.xlims[2] - imap.xlims[1]) / nb_subs
		delta_y = (imap.ylims[2] - imap.ylims[1]) / nb_subs
		for xindex in 1:nb_subs, yindex in 1:nb_subs
			local_xlims = (imap.xlims[1] + (xindex-1)*delta_x,  imap.xlims[1] + (xindex)*delta_x)
			local_ylims = (imap.ylims[2] - (yindex)*delta_y, imap.ylims[2] - (yindex-1)*delta_y)
			# this creates empty arrays for all the map properties
			tm.map_dict[(zoom_level, xindex, yindex)] = ScatterMap(local_xlims, local_ylims)
		end
	end
	
	for zoom_level in 1:zoom_levels
		nb_subs = 2^(zoom_level-1)
		delta_x = (imap.xlims[2] - imap.xlims[1]) / nb_subs
		delta_y = (imap.ylims[2] - imap.ylims[1]) / nb_subs
		for xindex in 1:nb_subs, yindex in 1:nb_subs
			for i in 1:size(imap.xys, 1)
				(xmin, xmax) = tm.map_dict[(zoom_level, xindex, yindex)].xlims
				(ymin, ymax) = tm.map_dict[(zoom_level, xindex, yindex)].ylims
				
				if xmin - delta_x/10 <= imap.xys[i][1] && imap.xys[i][1] <= xmax+delta_x/10 &&
					ymin -delta_x/10 <= imap.xys[i][2] && imap.xys[i][2] <= ymax+delta_x/10
					push!(tm.map_dict[(zoom_level, xindex, yindex)].xys, (imap.xys[i][1], imap.xys[i][2]))
					push!(tm.map_dict[(zoom_level, xindex, yindex)].colors, imap.colors[i])
					push!(tm.map_dict[(zoom_level, xindex, yindex)].sizes, imap.sizes[i])
				end

				# NB: for text, to prevent clipping, we also add all the labels
				# in the neighboring tiles!
				if markersize[i] > marker_size_limit[max(1, zoom_level-1)] +1 && 
					xmin - delta_x < imap.xys[i][1] &&
					imap.xys[i][1] <= xmax + delta_x &&
					ymin - delta_y <= imap.xys[i][2] &&
					imap.xys[i][2] < ymax + delta_y

					push!(tm.map_dict[(zoom_level, xindex, yindex)].labels,
	   					(imap.labels[i])) 
				end
			end
		end
	end
	tm
end
			  
function plot_sm(sm::ScatterMap, filename::String; kwargs...)
	scatter(sm.xys,
	 color = sm.colors,
	 markersize = sm.sizes,
	 xlims = sm.xlims,
	 ylims = sm.ylims,
	 grid = false,
	 axis = false,
	 legend = false,
	 margin = 0mm;
	 kwargs...);
	annotate!(sm.labels);
	png(filename)
end
"""
returns an empty png!
"""
function plot_sm(filename::String)
	scatter([(0,0)], grid = false, axis = false, legend = false, margin = 0mm);
	png(filename)
end

function plot_tm(tm::TiledMap, base_directory::String; kwargs...)
	file_number, directory_index = 0, 0

	# normalizing directory string and checking for existence
	endswith(base_directory, "/") && (base_directory = base_directory[1:end-1])
	isdir(base_directory) || error(base_directory * " is not a directory")
	
	isdir(base_directory * "/TileGroup" * string(directory_index)) || mkdir(base_directory * "/TileGroup" * string(directory_index))
	
	for d in 1:tm.depth
		nb_subs = 2^(d-1)
		for xi in 1:nb_subs, yi in 1:nb_subs
			filename = base_directory * "/TileGroup" * string(directory_index) * "/"  *
				string(d-1) * "-" * string(xi-1) * "-" * string(yi-1)
			if length(tm.map_dict[d, xi, yi].xys) > 0
				plot_sm(tm.map_dict[d, xi, yi], filename; kwargs...)
			else
				plot_sm(filename) # empty plot
			end
			file_number += 1
			if Int(floor(file_number/1024)) != directory_index
				directory_index += 1
				isdir(base_directory * "/TileGroup" * string(directory_index)) || mkdir(base_directory * "/TileGroup" * string(directory_index))
			end
		end
	end
end
end
