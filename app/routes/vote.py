from flask import request, g, abort

from app.controllers import vote
from app.server import server
from app.helpers.render import render_json


@server.route("/votes/post/<int:post_id>")
def post_votes(post_id):
    return render_json(vote.get_post_vote_breakdown(post_id))


@server.route("/votes/answer/<int:answer_id>")
def answer_votes(answer_id):
    return render_json(vote.get_answer_vote_breakdown(answer_id))


@server.route("/vote/post/<int:post_id>", methods=['GET', 'POST'])
def post_vote(post_id):
    if request.method == 'GET':
        return render_json(vote.get_post_vote(post_id))
    json = request.get_json(silent=True)
    if json is None:
        return abort(400)
    vote_data = json['vote']
    return render_json(vote.do_post_vote(post_id, vote_data))


@server.route("/vote/answer/<int:answer_id>", methods=['GET', 'POST'])
def answer_vote(answer_id):
    if request.method == 'GET':
        return render_json(vote.get_answer_vote(answer_id))
    json = request.get_json(silent=True)
    if json is None:
        return abort(400)
    vote_data = json['vote']
    return render_json(vote.do_answer_vote(answer_id, vote_data))
