from flask import Blueprint, request, jsonify
from app import db
from app.models.items import Item
from sqlalchemy import func

search_bp = Blueprint("search", __name__)


@search_bp.route("/search", methods=["GET"])
def search():
    query = db.session.query(Item)
    title = request.args.get("title")
    url = request.args.get("url")
    date_after = request.args.get("date_after")
    date_before = request.args.get("date_before")
    date_start = request.args.get("date_start")
    date_end = request.args.get("date_end")

    # Title search: case-insensitive, full or partial matches
    if title:
        query = query.filter(Item.title.ilike(f"%{title}%"))

    # URL search: full or partial matches
    if url:
        query = query.filter(Item.url.ilike(f"%{url}%"))

    # Date range search: after a specific date
    if date_after:
        query = query.filter(Item.date_added > func.date(date_after))

    # Date range search: before a specific date
    if date_before:
        query = query.filter(Item.date_added < func.date(date_before))

    # Date range search: between two dates
    if date_start and date_end:
        query = query.filter(
            Item.date_added >= func.date(date_start),
            Item.date_added <= func.date(date_end),
        )

    results = query.all()
    return jsonify([item.to_dict() for item in results])
