export default function (CompositeService, objectKey, nestedService) {
    let nested = nestedService(CompositeService.getAxios())
    CompositeService[objectKey] = nested(CompositeService.getResource())
    return CompositeService
}
