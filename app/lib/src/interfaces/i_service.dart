abstract class IService<M> {
  Future<List<M>> getAll(String endpoint, {Map<String, dynamic> params});
  Future<M> getOne(String endpoint, {Map<String, dynamic> params});
  Future<String> post(String endpoint);
  Future<M> postData(String endpoint, {Map<String, dynamic> params});
  Future<M> putData(String endpoint, {Map<String, dynamic> params});
  Future<M> patchData(String endpoint, {Map<String, dynamic> params});
  Future<String> delete(String endpoint);
}
