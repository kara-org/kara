abstract class IService<M> {
  Future<List<M>> getAll(endpoint, {params});
  Future<M> getOne(endpoint, {params});
  Future<M> postData(endpoint, {params});
  Future<M> putData(endpoint, {params});
  Future<M> patchData(endpoint, {params});
  Future<M> deleteData(endpoint, {params});
}