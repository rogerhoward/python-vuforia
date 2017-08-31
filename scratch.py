    # def get_target_by_id(self, target_id):
    #     url = '%s/targets/%s' % (self.host, target_id)
    #     req = urllib.request.Request(url)
    #     response = self._get_authenticated_response(req)
    #     return json.loads(response.read())['target_record']

    # def get_target_ids(self):
    #     url = '%s/targets' % self.host
    #     req = urllib.request.Request(url)
    #     response = self._get_authenticated_response(req)
    #     return json.loads(response.read())['results']

    # def get_summary(self):
    #     url = '%s/summary' % self.host
    #     req = urllib.request.Request(url)
    #     response = self._get_authenticated_response(req)
    #     return json.loads(response.read())

    # def get_targets(self):
    #     targets = []
    #     for target_id in self.get_target_ids():
    #         targets.append(self.get_target_by_id(target_id))
    #     return targets

    # def add_target(self, data):
    #     url = '%s/targets' % self.host
    #     data = json.dumps(data)
    #     req = urllib.request.Request(url, data, {'Content-Type': 'application/json; charset=utf-8'})
    #     response = self._get_authenticated_response(req)
    #     return json.loads(response.read())

    # def update_target(self, target_id, data):
    #     # Takes time to process
    #     url = '%s/targets/%s' % (self.host, target_id)
    #     data = json.dumps(data)
    #     req = urllib.request.Request(url, data, {'Content-Type': 'application/json; charset=utf-8'})
    #     req.get_method = lambda: 'PUT'
    #     response = self._get_authenticated_response(req)
    #     return json.loads(response.read())

    # def delete_target(self, target_id):
    #     # Takes time to process
    #     url = '%s/targets/%s' % (self.host, target_id)
    #     req = urllib.request.Request(url)
    #     req.get_method = lambda: 'DELETE'
    #     response = self._get_authenticated_response(req)
    #     return json.loads(response.read())