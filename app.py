from flask import Flask, request, jsonify, make_response

# Initialize Flask app
app = Flask(__name__)

# Application name: EPA Kuwait

# Example database (to be expanded)
data = {
    "laws": [
        {
            "id": 1,
            "title": "قانون حماية البيئة رقم 42 لسنة 2014",
            "description": "القانون الأساسي لحماية البيئة في الكويت.",
            "related_executive_decisions": [
                {
                    "title": "قرار رقم 12 لسنة 2017",
                    "details": "حماية البيئة المائية والساحلية من التلوث."
                }
            ],
            "related_international_agreements": [
                {
                    "title": "اتفاقية الكويت الإقليمية لحماية البيئة البحرية",
                    "details": "تنظيم حماية البيئة البحرية في المنطقة."
                }
            ],
            "violations": [
                {
                    "type": "تلويث المياه البحرية",
                    "penalties": "غرامة تصل إلى 100,000 دينار كويتي مع تحمل تكاليف التنظيف."
                }
            ]
        }
    ]
}

# Route for the home page
@app.route("/")
def home():
    return "Welcome to EPA Kuwait!"

# Route for search functionality
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "No query provided."}), 400

    # Search logic (simplified for demonstration)
    results = []
    for law in data["laws"]:
        context = law["description"] + ". "
        for decision in law["related_executive_decisions"]:
            context += decision["title"] + ": " + decision["details"] + ". "
        for agreement in law["related_international_agreements"]:
            context += agreement["title"] + ": " + agreement["details"] + ". "
        for violation in law["violations"]:
            context += violation["type"] + ": " + violation["penalties"] + ". "

        if query.lower() in context.lower():
            results.append({"law": law["title"], "context": context})

    # Create response with correct encoding
    response = make_response(jsonify(results))
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

# Main block to run the app
if __name__ == "__main__":
    app.run(debug=True)
