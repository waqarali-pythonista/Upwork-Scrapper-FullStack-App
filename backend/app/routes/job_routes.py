from flask import Blueprint, jsonify, request
from app.services.scraper_service import ScraperService
from app.models.job_model import Job
from app import db

job_bp = Blueprint('job', __name__)

# Route to scrape and store data
@job_bp.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    scraper = ScraperService(url)
    try:
        job_title, description = scraper.scrape()

        # Save to the database
        job = Job(job_title=job_title, description=description)
        db.session.add(job)
        db.session.commit()

        return jsonify({"job_title": job_title, "description": description})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all jobs
@job_bp.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        jobs = Job.query.all()
        jobs_data = [{"id": job.id, "job_title": job.job_title, "description": job.description} for job in jobs]
        return jsonify(jobs_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
