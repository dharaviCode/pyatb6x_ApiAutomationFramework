#In this file we will have a class
# which keeps all our (API http method) api endpoints under created functions:

class APIConstants:

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    # Update -> PUT, PATCH, DELETE - booking_id

    def url_patch_put_delete(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

