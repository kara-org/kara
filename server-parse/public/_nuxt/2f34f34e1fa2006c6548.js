(window.webpackJsonp=window.webpackJsonp||[]).push([[10],{838:function(e,t,r){"use strict";var o=r(3),c=r(845);o.a.directive("cleave",{bind:function(e,t){var input=e.querySelector("input");input._vCleave=new c.a(input,t.value)},unbind:function(e){e.querySelector("input")._vCleave.destroy()}})},842:function(e,t,r){var content=r(857);"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,r(87).default)("67bb96c3",content,!0,{sourceMap:!1})},856:function(e,t,r){"use strict";var o=r(842);r.n(o).a},857:function(e,t,r){(t=r(86)(!1)).push([e.i,".page-enter-active[data-v-ce339ee0],.page-leave-active[data-v-ce339ee0]{transition:opacity .3s ease}.page-enter[data-v-ce339ee0],.page-leave-to[data-v-ce339ee0]{opacity:0}.is-degrade-primary[data-v-ce339ee0]{background:linear-gradient(-87deg,rgba(26,188,156,.8),rgba(46,204,113,.8))}a[data-v-ce339ee0]{color:#20c090}h1[data-v-ce339ee0]{padding-top:1.5em}h1.is-primary[data-v-ce339ee0]{color:#20c090}h1.is-centered[data-v-ce339ee0]{text-align:center}.form-section-title[data-v-ce339ee0]{text-align:center;font-weight:700;font-size:1.2em}.button.is-primary[data-v-ce339ee0]{background-color:#20c090}.button.is-primary.is-outlined[data-v-ce339ee0]{background-color:transparent;border-color:#20c090;color:#20c090}.button.is-primary.is-outlined.is-focused[data-v-ce339ee0],.button.is-primary.is-outlined.is-hovered[data-v-ce339ee0],.button.is-primary.is-outlined[data-v-ce339ee0]:focus,.button.is-primary.is-outlined[data-v-ce339ee0]:hover{background-color:#20c090;border-color:#20c090;color:#fff}.navbar-link.is-active[data-v-ce339ee0],.navbar-link[data-v-ce339ee0]:focus,.navbar-link[data-v-ce339ee0]:hover,.navbar-link[focus-within][data-v-ce339ee0],a.navbar-item.is-active[data-v-ce339ee0],a.navbar-item[data-v-ce339ee0]:focus,a.navbar-item[data-v-ce339ee0]:hover,a.navbar-item[focus-within][data-v-ce339ee0]{color:#20c090}.navbar-link.is-active[data-v-ce339ee0],.navbar-link[data-v-ce339ee0]:focus,.navbar-link[data-v-ce339ee0]:focus-within,.navbar-link[data-v-ce339ee0]:hover,a.navbar-item.is-active[data-v-ce339ee0],a.navbar-item[data-v-ce339ee0]:focus,a.navbar-item[data-v-ce339ee0]:focus-within,a.navbar-item[data-v-ce339ee0]:hover{color:#20c090}.tag:not(body).is-primary[data-v-ce339ee0]{background-color:#20c090}.has-text-primary[data-v-ce339ee0]{color:#20c090!important}.menu-list a.is-active[data-v-ce339ee0]{background-color:#20c090}.button.is-primary.is-hovered[data-v-ce339ee0],.button.is-primary[data-v-ce339ee0]:hover{background-color:#20a0a0}.button:not(.is-outlined).is-primary.is-active[data-v-ce339ee0],.button:not(.is-outlined).is-primary[data-v-ce339ee0]:active{background-color:#20c090}.button.is-primary[disabled][data-v-ce339ee0],fieldset[disabled] .button.is-primary[data-v-ce339ee0]{background-color:#108080}.pagination-link.is-current[data-v-ce339ee0]{background-color:#20c090;border-color:#20c090}.pagination-link[data-v-ce339ee0]:focus,.pagination-next[data-v-ce339ee0]:focus,.pagination-previous[data-v-ce339ee0]:focus{border-color:#20c090}.has-background-primary[data-v-ce339ee0]{background-color:#20c090!important}.tabs.is-toggle li.is-active a[data-v-ce339ee0]{background-color:#20c090;border-color:#20c090}.input[data-v-ce339ee0]:active,.input[data-v-ce339ee0]:focus,.is-active.input[data-v-ce339ee0],.is-active.textarea[data-v-ce339ee0],.is-focused.input[data-v-ce339ee0],.is-focused.textarea[data-v-ce339ee0],.select select.is-active[data-v-ce339ee0],.select select.is-focused[data-v-ce339ee0],.select select[data-v-ce339ee0]:active,.select select[data-v-ce339ee0]:focus,.taginput .is-active.taginput-container.is-focusable[data-v-ce339ee0],.taginput .is-focused.taginput-container.is-focusable[data-v-ce339ee0],.taginput .taginput-container.is-focusable[data-v-ce339ee0]:active,.taginput .taginput-container.is-focusable[data-v-ce339ee0]:focus,.textarea[data-v-ce339ee0]:active,.textarea[data-v-ce339ee0]:focus{border-color:#20c090;box-shadow:0 0 0 .125em rgba(82,164,137,.25)}.profile-image[data-v-ce339ee0]{border-radius:50%!important;width:128px;height:128px;-o-object-fit:cover;object-fit:cover}",""]),e.exports=t},867:function(e,t,r){var content=r(898);"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,r(87).default)("de4d477e",content,!0,{sourceMap:!1})},879:function(e,t,r){"use strict";r(162),r(54),r(55),r(38),r(128),r(163),r(30);var o=r(0),c=r(70),n=(r(838),r(110),r(88));function d(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}var l={props:{isCadastro:Boolean,isDoador:Boolean},data:function(){return{usuario:{email:null,password:null,nome:null,telefones:[null]},passwordConfirm:null,success:!1,phoneMask:{delimiters:["(",")"," ","-"],blocks:[0,2,0,4,5],numericOnly:!0},isLoading:null}},created:function(){this.isCadastro||(this.usuario=this.$store.state.login.usuario)},methods:function(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?d(Object(source),!0).forEach((function(t){Object(c.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):d(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}({},Object(n.b)({signUpParse:"login/signUp",updateParse:"login/update"}),{register:function(){var e=this;return Object(o.a)(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,e.signUpParse({email:e.usuario.email,password:e.usuario.password,nome:e.usuario.nome,telefones:e.usuario.telefones}).then((function(t){e.$buefy.toast.open({message:"Cadastro realizado com successo!",type:"is-success",position:"is-top"}),e.$router.push("/")})).catch((function(t){console.log(t),202==t.code&&(t.message="Usuário com este email já existe"),e.$buefy.toast.open({message:t.message,type:"is-danger",position:"is-bottom"})}));case 2:e.isLoading=!1;case 3:case"end":return t.stop()}}),t)})))()},patch:function(){var e=this;return Object(o.a)(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,e.updateParse({email:e.usuario.email,nome:e.usuario.nome,telefones:e.usuario.telefones}).then((function(t){e.$buefy.toast.open({message:"Alteração realizada com successo!",type:"is-success",position:"is-top"})})).catch((function(t){console.log(t),202==t.code&&(t.message="Usuário com este email já existe"),e.$buefy.toast.open({message:t.message,type:"is-danger",position:"is-bottom"})}));case 2:e.success=!0,e.isLoading=!1;case 4:case"end":return t.stop()}}),t)})))()},validateBeforeSubmit:function(){var e=this;this.$validator.validateAll().then((function(t){if(t)return e.usuario.telefones[0]=e.usuario.telefones[0].replace(/\D/g,""),e.isLoading=!0,e.isCadastro?e.register():e.patch();e.$buefy.toast.open({message:"Formulário inválido, verifique os campos em vermelho",type:"is-danger",position:"is-bottom"})}))}})},v=(r(856),r(29)),component=Object(v.a)(l,(function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("section",[e.success?r("div",{staticClass:"column has-text-centered"},[r("h1",[e._v("Atualização realizada com sucesso!")]),e._v(" "),r("hr"),e._v(" "),r("button",{staticClass:"button is-primary is-outlined is-rounded",attrs:{"exact-active-class":"is-active"},on:{click:function(t){e.success=!1}}},[e._v("Voltar")])]):r("form",{attrs:{method:"post"},on:{submit:function(t){return t.preventDefault(),e.validateBeforeSubmit(t)}}},[r("hr"),e._v(" "),r("b-field",{attrs:{label:"Nome",type:{"is-danger":e.errors.has("nome")},message:e.errors.first("nome")}},[r("b-input",{directives:[{name:"validate",rawName:"v-validate",value:"required",expression:"'required'"}],attrs:{type:"text",name:"nome"},model:{value:e.usuario.nome,callback:function(t){e.$set(e.usuario,"nome","string"==typeof t?t.trim():t)},expression:"usuario.nome"}})],1),e._v(" "),r("b-field",{attrs:{label:"Telefone",type:{"is-danger":e.errors.has("telefone")},message:e.errors.first("telefone")}},[r("b-input",{directives:[{name:"cleave",rawName:"v-cleave",value:e.phoneMask,expression:"phoneMask"},{name:"validate",rawName:"v-validate",value:"required|phone",expression:"'required|phone'"}],attrs:{type:"text",maxlength:"15",name:"telefone"},model:{value:e.usuario.telefones[0],callback:function(t){e.$set(e.usuario.telefones,0,"string"==typeof t?t.trim():t)},expression:"usuario.telefones[0]"}})],1),e._v(" "),r("b-field",{attrs:{label:"Email",type:{"is-danger":e.errors.has("email")},message:e.errors.first("email")}},[r("b-input",{directives:[{name:"validate",rawName:"v-validate",value:"required|email",expression:"'required|email'"}],attrs:{type:"text",name:"email"},model:{value:e.usuario.email,callback:function(t){e.$set(e.usuario,"email","string"==typeof t?t.trim():t)},expression:"usuario.email"}})],1),e._v(" "),e.isCadastro?[r("b-field",{attrs:{label:"Senha",type:{"is-danger":e.errors.has("senha")},message:e.errors.first("senha")}},[r("b-input",{directives:[{name:"validate",rawName:"v-validate",value:"required|min:4",expression:"'required|min:4'"}],ref:"senha",attrs:{type:"password",name:"senha"},model:{value:e.usuario.password,callback:function(t){e.$set(e.usuario,"password",t)},expression:"usuario.password"}})],1),e._v(" "),r("b-field",{attrs:{label:"Confirme sua senha",type:{"is-danger":e.errors.has("confirmação")},message:e.errors.first("confirmação")}},[r("b-input",{directives:[{name:"validate",rawName:"v-validate",value:"required|confirmed:senha",expression:"'required|confirmed:senha'"}],attrs:{name:"confirmação",type:"password"},model:{value:e.passwordConfirm,callback:function(t){e.passwordConfirm=t},expression:"passwordConfirm"}})],1),e._v(" "),r("hr"),e._v(" "),r("div",{staticClass:"column has-text-centered"},[e._v("\n        Já tem um cadastro?\n        "),r("nuxt-link",{staticClass:"is-primary is-inverted",attrs:{to:"/auth/login","exact-active-class":"is-active"}},[e._v("Logue-se")])],1)]:e._e(),e._v(" "),r("hr"),e._v(" "),r("button",{staticClass:"button is-primary is-outlined is-medium is-rounded is-fullwidth",attrs:{type:"submit"}},[e._v("\n      Confirmar\n      "),r("b-loading",{attrs:{"is-full-page":!0,active:e.isLoading,"can-cancel":!1},on:{"update:active":function(t){e.isLoading=t}}})],1),e._v(" "),r("div",{staticClass:"column has-text-centered"},[r("nuxt-link",{staticClass:"voltar is-primary is-inverted",attrs:{to:"/","exact-active-class":"is-active"}},[e._v("Voltar")])],1)],2)])}),[],!1,null,"ce339ee0",null);t.a=component.exports},897:function(e,t,r){"use strict";var o=r(867);r.n(o).a},898:function(e,t,r){(t=r(86)(!1)).push([e.i,".page-enter-active[data-v-0dfc12e4],.page-leave-active[data-v-0dfc12e4]{transition:opacity .3s ease}.page-enter[data-v-0dfc12e4],.page-leave-to[data-v-0dfc12e4]{opacity:0}.is-degrade-primary[data-v-0dfc12e4]{background:linear-gradient(-87deg,rgba(26,188,156,.8),rgba(46,204,113,.8))}a[data-v-0dfc12e4]{color:#20c090}h1[data-v-0dfc12e4]{padding-top:1.5em}h1.is-primary[data-v-0dfc12e4]{color:#20c090}h1.is-centered[data-v-0dfc12e4]{text-align:center}.form-section-title[data-v-0dfc12e4]{text-align:center;font-weight:700;font-size:1.2em}.button.is-primary[data-v-0dfc12e4]{background-color:#20c090}.button.is-primary.is-outlined[data-v-0dfc12e4]{background-color:transparent;border-color:#20c090;color:#20c090}.button.is-primary.is-outlined.is-focused[data-v-0dfc12e4],.button.is-primary.is-outlined.is-hovered[data-v-0dfc12e4],.button.is-primary.is-outlined[data-v-0dfc12e4]:focus,.button.is-primary.is-outlined[data-v-0dfc12e4]:hover{background-color:#20c090;border-color:#20c090;color:#fff}.navbar-link.is-active[data-v-0dfc12e4],.navbar-link[data-v-0dfc12e4]:focus,.navbar-link[data-v-0dfc12e4]:hover,.navbar-link[focus-within][data-v-0dfc12e4],a.navbar-item.is-active[data-v-0dfc12e4],a.navbar-item[data-v-0dfc12e4]:focus,a.navbar-item[data-v-0dfc12e4]:hover,a.navbar-item[focus-within][data-v-0dfc12e4]{color:#20c090}.navbar-link.is-active[data-v-0dfc12e4],.navbar-link[data-v-0dfc12e4]:focus,.navbar-link[data-v-0dfc12e4]:focus-within,.navbar-link[data-v-0dfc12e4]:hover,a.navbar-item.is-active[data-v-0dfc12e4],a.navbar-item[data-v-0dfc12e4]:focus,a.navbar-item[data-v-0dfc12e4]:focus-within,a.navbar-item[data-v-0dfc12e4]:hover{color:#20c090}.tag:not(body).is-primary[data-v-0dfc12e4]{background-color:#20c090}.has-text-primary[data-v-0dfc12e4]{color:#20c090!important}.menu-list a.is-active[data-v-0dfc12e4]{background-color:#20c090}.button.is-primary.is-hovered[data-v-0dfc12e4],.button.is-primary[data-v-0dfc12e4]:hover{background-color:#20a0a0}.button:not(.is-outlined).is-primary.is-active[data-v-0dfc12e4],.button:not(.is-outlined).is-primary[data-v-0dfc12e4]:active{background-color:#20c090}.button.is-primary[disabled][data-v-0dfc12e4],fieldset[disabled] .button.is-primary[data-v-0dfc12e4]{background-color:#108080}.pagination-link.is-current[data-v-0dfc12e4]{background-color:#20c090;border-color:#20c090}.pagination-link[data-v-0dfc12e4]:focus,.pagination-next[data-v-0dfc12e4]:focus,.pagination-previous[data-v-0dfc12e4]:focus{border-color:#20c090}.has-background-primary[data-v-0dfc12e4]{background-color:#20c090!important}.tabs.is-toggle li.is-active a[data-v-0dfc12e4]{background-color:#20c090;border-color:#20c090}.input[data-v-0dfc12e4]:active,.input[data-v-0dfc12e4]:focus,.is-active.input[data-v-0dfc12e4],.is-active.textarea[data-v-0dfc12e4],.is-focused.input[data-v-0dfc12e4],.is-focused.textarea[data-v-0dfc12e4],.select select.is-active[data-v-0dfc12e4],.select select.is-focused[data-v-0dfc12e4],.select select[data-v-0dfc12e4]:active,.select select[data-v-0dfc12e4]:focus,.taginput .is-active.taginput-container.is-focusable[data-v-0dfc12e4],.taginput .is-focused.taginput-container.is-focusable[data-v-0dfc12e4],.taginput .taginput-container.is-focusable[data-v-0dfc12e4]:active,.taginput .taginput-container.is-focusable[data-v-0dfc12e4]:focus,.textarea[data-v-0dfc12e4]:active,.textarea[data-v-0dfc12e4]:focus{border-color:#20c090;box-shadow:0 0 0 .125em rgba(82,164,137,.25)}.hero-body[data-v-0dfc12e4]{padding-top:1em!important}.columns div[data-v-0dfc12e4]{margin:10px!important}",""]),e.exports=t},924:function(e,t,r){"use strict";r.r(t);var o=r(879),c=r(266),n={layout:"default",components:{CadastroDoadorForm:o.a,MenuLateral:c.a}},d=(r(897),r(29)),component=Object(d.a)(n,(function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"columns is-fullheight"},[t("MenuLateral",{attrs:{isDoador:!0}}),this._v(" "),t("section",{staticClass:"column is-main-content hero is-medium is-bold",staticStyle:{"align-items":"center"}},[t("div",{staticClass:"hero-body"},[t("article",{staticClass:"card is-rounded",staticStyle:{width:"600px"}},[t("div",{staticClass:"card-content"},[t("p",{staticClass:"form-section-title"},[this._v("Edite suas informações")]),this._v(" "),t("CadastroDoadorForm",{attrs:{isCadastro:!1}})],1)])])])],1)}),[],!1,null,"0dfc12e4",null);t.default=component.exports}}]);