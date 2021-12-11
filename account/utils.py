from datetime import datetime


def check_token_expiration(token):

	token_creation_time = datetime.fromtimestamp(token.created_at)
	current_time = datetime.now()
	diff = current_time - token_creation_time
	diff_in_seconds = diff.total_seconds()

	return diff_in_seconds