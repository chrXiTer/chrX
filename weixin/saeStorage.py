from sae import storage

class saeStorage(object):
    def __init__(self, bucketName):
        access_key =storage.ACCESS_KEY
        secret_key = storage.SECRET_KEY
        app_name = storage.APP_NAME
        connection = storage.Connection(access_key, secret_key, app_name)
        self._bucket = connection.get_bucket(bucketName)

    def save(self, filename, data, contentType=None):
        return self._bucket.put_object(filename, data, contentType)

    def delete(self, filename, data):
        return self._bucket.delete_object(filename)

    def getUrl(self, filename):
        return self._bucket.generate_url(filename)