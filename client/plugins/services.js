import createService from '~/services/ServiceBase'
import composite from '~/services/composite'
import doacoesService from '~/services/DoacoesService'
// import buscarServiceBase from '~/services/BuscarService'


export default (ctx, inject) => {
  // inject the repository in the context (ctx.app.$repository)
  // And in the Vue instances (this.$repository in your components)

  const serviceDefault = createService({ $axios: ctx.$axios, $store: ctx.app.$store });
  // const buscarService  = buscarServiceBase(ctx.$axios);

  const serviceOng = composite(serviceDefault('/ong/'), "$doacoes", doacoesService);
  const serviceDoador = composite(serviceDefault('/doador/'),"$doacoes", doacoesService);

  // ex.: inject('NovoService', serviceDefault('/url/'));
  inject('UsuarioService', serviceDefault('/usuario/'));
  inject('DoacaoService', serviceDefault('/doacao/'));
  inject('OngService', serviceOng);
  inject('DoadorService', serviceDoador);
  // inject('BuscarService', buscarService);



}

