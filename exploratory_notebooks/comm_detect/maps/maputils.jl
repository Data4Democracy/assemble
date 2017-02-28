module MapUtils
using Plots


export create_data_dict


"""
This function takes in a number of zoom levels, a set of xlims and ylims,
an array of tuples representing the data, an array of colors representing 
some factor of the data, an array of sizes representing the data,
and a set of labels.

It will return a dictionary indexed by (zoom_level, xindex, yindex),
where xindex and yindex are dependent on the zoom level and represent the indices
of the tile for which the data is needed.
"""
function create_data_dict(zoom_levels::Int64,
			  xlims::Tuple{Float64, Float64},
			  ylims::Tuple{Float64, Float64},
			  data::Array{Tuple{Float64, Float64}},
			  color_data::Array{ColorTypes.RGBA{Float64}, 1},
			  markersize::Array{Float64, 1},
			  names::Array{String, 1})

	marker_size_limit = quantile(markersize, [max(0,1-10*4^(zoom_level+1)/1000000) for zoom_level in 0:zoom_levels])
	coord_dic = Dict{Tuple{Int64,Int64, Int64}, Array{Tuple{Float64, Float64},1}}()
	color_dic = Dict{Tuple{Int64,Int64, Int64}, Array{ColorTypes.RGBA{Float64},1}}()
	size_dic = Dict{Tuple{Int64,Int64, Int64}, Array{Float64,1}}()
	name_dic = Dict{Tuple{Int64,Int64, Int64}, Array{Tuple{Float64, Float64, String},1}}()

	for zoom_level in 2:zoom_levels
		nb_subs = 2^(zoom_level-1)
		for xindex in 1:nb_subs, yindex in 1:nb_subs
			coord_dic[(zoom_level, xindex, yindex)] = []
			color_dic[(zoom_level, xindex, yindex)] = []
			size_dic[(zoom_level, xindex, yindex)] = []
			name_dic[(zoom_level, xindex, yindex)] = []
		end
	end

	for zoom_level in 2:zoom_levels
		nb_subs = 2^(zoom_level-1)
		delta_x = (xlims[2] - xlims[1]) / nb_subs
		delta_y = (ylims[2] - ylims[1]) / nb_subs
		for xindex in 1:nb_subs, yindex in 1:nb_subs
			local_xmin = xlims[1] + (xindex-1)*delta_x
			local_xmax = xlims[1] + (xindex)*delta_x
			local_ymin = ylims[2] - (yindex)*delta_y
			local_ymax = ylims[2] - (yindex-1)*delta_y
			for i in 1:size(data, 1)
				if local_xmin < data[i][1] && data[i][1] <= local_xmax &&
					local_ymin < data[i][2] && data[i][2] <= local_ymax
					push!(coord_dic[(zoom_level, xindex, yindex)], (data[i][1], data[i][2]))
					push!(color_dic[(zoom_level, xindex, yindex)], color_data[i])
					push!(size_dic[(zoom_level, xindex, yindex)], markersize[i])
				end
				if markersize[i] > marker_size_limit[zoom_level-1] +1 && 
					local_xmin - delta_x < data[i][1] &&
					data[i][1] <= local_xmax + delta_x &&
					local_ymin - delta_y <= data[i][2] &&
					data[i][2] < local_ymax + delta_y

					push!(name_dic[(zoom_level, xindex, yindex)], (data[i][1], data[i][2]))
				end
			end
		end
	end

	return coord_dic, color_dic, size_dic, name_dic
end
			  


end
