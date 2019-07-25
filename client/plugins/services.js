import createService from '~/services/ServiceBase'
import composite from '~/services/composite'
import doacoesService from '~/services/DoacoesService'


export default (ctx, inject) => {
  // inject the repository in the context (ctx.app.$repository)
  // And in the Vue instances (this.$repository in your components)
  const serviceDefault = createService(ctx.$axios)

  const serviceOng = composite(serviceDefault('/ong/'), "$doacoes", doacoesService)
  const serviceDoador = composite(serviceDefault('/doador/'),"$doacoes", doacoesService)

  inject('UsuarioService', serviceDefault('/usuario/'))
  inject('NovoService', serviceDefault('/url/'))
  inject('OngService', serviceOng)
  inject('DoadorService', serviceDoador)



}
