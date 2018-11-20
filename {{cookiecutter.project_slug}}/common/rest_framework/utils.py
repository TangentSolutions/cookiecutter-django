class CommonResponses:
    @property
    def missing_permission(self):
        return {"detail": "You do not have permission to perform this action."}

    @property
    def missing_authentication(self):
        return {"detail": "Authentication credentials were not provided."}
