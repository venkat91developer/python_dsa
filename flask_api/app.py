import networkx as nx
import osmnx as ox
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__)
CORS(app, resources={r"/shortest_path": {"origins": "*"}})  # Enable CORS for the specific route

# Load and prepare the graph once at startup
G = ox.graph_from_place('Manhattan, New York, USA', network_type='drive')
G = ox.project_graph(G)

@app.route('/shortest_path', methods=['GET'])
def shortest_path():
    start_lat = float(request.args.get('start_lat'))
    start_lng = float(request.args.get('start_lng'))
    end_lat = float(request.args.get('end_lat'))
    end_lng = float(request.args.get('end_lng'))

    # Find the nearest nodes for the start and end locations
    start_node = ox.nearest_nodes(G, X=start_lng, Y=start_lat)
    end_node = ox.nearest_nodes(G, X=end_lng, Y=end_lat)

    try:
        # Find the shortest path using Dijkstra's algorithm
        path = nx.dijkstra_path(G, source=start_node, target=end_node, weight='length')
        path_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in path]
        return jsonify({'path': path_coords})
    except nx.NetworkXNoPath:
        return jsonify({'error': 'No path found'}), 404

if __name__ == '__main__':
    app.run(debug=True,port=5001)
