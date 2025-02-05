from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, Client

app = Flask(__name__)
api = Api(app)
CORS(app)  # Allow frontend to access API

# Create Client (POST)
class CreateClient(Resource):
    def post(self):
        data = request.get_json()
        new_client = Client(
            name=data["name"],
            email=data["email"],
            phone=data.get("phone"),
            company=data.get("company"),
            notes=data.get("notes"),
        )
        db.session.add(new_client)
        db.session.commit()
        return jsonify({"message": "Client added successfully", "client": data})

# Get All Clients (GET)
class GetClients(Resource):
    def get(self):
        clients = Client.query.all()
        client_list = [
            {"id": c.id, "name": c.name, "email": c.email, "phone": c.phone, "company": c.company, "notes": c.notes}
            for c in clients
        ]
        return jsonify(client_list)

# Get Single Client (GET)
class GetClient(Resource):
    def get(self, client_id):
        client = Client.query.get(client_id)
        if not client:
            return jsonify({"error": "Client not found"}), 404
        return jsonify(
            {"id": client.id, "name": client.name, "email": client.email, "phone": client.phone, "company": client.company, "notes": client.notes}
        )

# Update Client (PUT)
class UpdateClient(Resource):
    def put(self, client_id):
        client = Client.query.get(client_id)
        if not client:
            return jsonify({"error": "Client not found"}), 404
        data = request.get_json()
        client.name = data.get("name", client.name)
        client.email = data.get("email", client.email)
        client.phone = data.get("phone", client.phone)
        client.company = data.get("company", client.company)
        client.notes = data.get("notes", client.notes)
        db.session.commit()
        return jsonify({"message": "Client updated successfully"})

# Delete Client (DELETE)
class DeleteClient(Resource):
    def delete(self, client_id):
        client = Client.query.get(client_id)
        if not client:
            return jsonify({"error": "Client not found"}), 404
        db.session.delete(client)
        db.session.commit()
        return jsonify({"message": "Client deleted successfully"})

# Register Routes
api.add_resource(CreateClient, "/clients")
api.add_resource(GetClients, "/clients/all")
api.add_resource(GetClient, "/clients/<int:client_id>")
api.add_resource(UpdateClient, "/clients/<int:client_id>/update")
api.add_resource(DeleteClient, "/clients/<int:client_id>/delete")
