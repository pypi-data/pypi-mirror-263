(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[1173],{57595:function(e,r,t){"use strict";var n=t(90849),i=t(34896),o=t(24246);function s(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}r.Z=function(e){return(0,o.jsx)(i.rU,function(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?s(Object(t),!0).forEach((function(r){(0,n.Z)(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):s(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}({isExternal:!0,color:"complimentary.500"},e))}},65535:function(e,r,t){"use strict";t.d(r,{ZS:function(){return c},a4:function(){return o}});var n=t(80406),i=t(28703).u.injectEndpoints({endpoints:function(e){return{getPurposes:e.query({query:function(){return"purposes"}})}}}),o=i.useGetPurposesQuery,s={purposes:{},special_purposes:{}},c=(0,n.P1)(i.endpoints.getPurposes.select(),(function(e){return e.data||s}))},24753:function(e,r,t){"use strict";t.d(r,{MA:function(){return u},Vo:function(){return p},t5:function(){return d}});var n=t(90849),i=t(34896),o=t(24246);function s(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function c(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?s(Object(t),!0).forEach((function(r){(0,n.Z)(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):s(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}var a=function(e){var r=e.children;return(0,o.jsxs)(i.xv,{"data-testid":"toast-success-msg",children:[(0,o.jsx)("strong",{children:"Success:"})," ",r]})},l=function(e){var r=e.children;return(0,o.jsxs)(i.xv,{"data-testid":"toast-error-msg",children:[(0,o.jsx)("strong",{children:"Error:"})," ",r]})},u={variant:"subtle",position:"top",description:"",duration:5e3,status:"success",isClosable:!0},d=function(e){var r=(0,o.jsx)(a,{children:e});return c(c({},u),{description:r})},p=function(e){var r=(0,o.jsx)(l,{children:e});return c(c({},u),{description:r,status:"error"})}},39732:function(e,r,t){"use strict";t.r(r),t.d(r,{default:function(){return G}});var n=t(90849),i=t(90089),o=t(73679),s=t(55732),c=t(97865),a=t(34707),l=t.n(a),u=t(70409),d=t(34896),p=t(83125),f=t(62709),h=t(29549),g=t(34090),b=t(27378),m=t(6848),x=t(57595),v=t(90768),j=t(78624),y=t(51471),O=t(65535),_=t(38687),w=t(24753),P=t(24246),C=function(e){var r=e.name,t=e.enabled;return(0,P.jsxs)(d.Kq,{spacing:2,fontSize:"sm",lineHeight:"5",fontWeight:"medium",color:"gray.700",children:[(0,P.jsxs)(d.xv,{children:[r," status"," ",t?(0,P.jsx)(d.Ct,{fontWeight:"semibold",color:"green.800",backgroundColor:"green.100",children:"Enabled"}):(0,P.jsx)(d.Ct,{fontWeight:"semibold",backgroundColor:"red.100",children:"Disabled"})]}),(0,P.jsxs)(d.xv,{children:["To ",t?"disable":"enable"," ",r,", please contact your Fides administrator or"," ",(0,P.jsx)(x.Z,{href:"mailto:support@ethyca.com",children:"Ethyca support"}),"."]})]})},S=t(43139),k=t(89403),E=t(9865),D=["title","children"];function T(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function I(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?T(Object(t),!0).forEach((function(r){(0,n.Z)(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):T(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}var z=function(e){var r=e.title,t=e.children,n=(0,i.Z)(e,D);return(0,P.jsxs)(d.xu,I(I({backgroundColor:"gray.50",borderRadius:"4px",padding:"3","data-testid":"setting-".concat(r)},n),{},{children:[(0,P.jsx)(d.xv,{fontSize:"md",fontWeight:"bold",lineHeight:5,color:"gray.700",mb:3,children:r}),t]}))},W=function(e){var r=e.title,t=e.children;return(0,P.jsxs)(d.Kq,{spacing:3,mb:3,"data-testid":"section-".concat(r),children:[(0,P.jsx)(d.xv,{fontSize:"sm",fontWeight:"bold",lineHeight:5,color:"gray.700",children:r}),t]})},F=function(){var e=(0,v.hz)().tcf,r=!!(0,m.C)(k.D2).enabled,t=(0,g.u6)().values,n=!!t.gpp.us_approach;return(0,P.jsx)(z,{title:"Global Privacy Platform",children:(0,P.jsxs)(d.Kq,{spacing:6,children:[(0,P.jsx)(C,{name:"GPP",enabled:r}),r?(0,P.jsxs)(P.Fragment,{children:[(0,P.jsx)(W,{title:"GPP U.S.",children:(0,P.jsx)(S.xt,{name:"gpp.us_approach",variant:"stacked",defaultFirstSelected:!1,options:[{label:"Enable U.S. National",value:E.en.NATIONAL,tooltip:"When US National is selected, Fides will present the same privacy notices to all consumers located anywhere in the United States."},{label:"Enable U.S. State-by-State",value:E.en.STATE,tooltip:"When state-by-state is selected, Fides will only present consent to consumers and save their preferences if they are located in a state that is supported by the GPP. The consent options presented to consumers will vary depending on the regulations in each state."}]})}),n?(0,P.jsxs)(W,{title:"MSPA",children:[(0,P.jsx)(S.Xl,{name:"gpp.mspa_covered_transactions",label:"All transactions covered by MSPA",tooltip:"When selected, the Fides CMP will communicate to downstream vendors that all preferences are covered under the MSPA."}),(0,P.jsx)(S.w8,{label:"Enable MSPA service provider mode",name:"gpp.mspa_service_provider_mode",variant:"switchFirst",tooltip:"Enable service provider mode if you do not engage in any sales or sharing of personal information.",isDisabled:t.gpp.mspa_opt_out_option_mode}),(0,P.jsx)(S.w8,{label:"Enable MSPA opt-out option mode",name:"gpp.mspa_opt_out_option_mode",variant:"switchFirst",tooltip:"Enable opt-out option mode if you engage or may engage in the sales or sharing of personal information, or process any information for the purpose of targeted advertising.",isDisabled:t.gpp.mspa_service_provider_mode})]}):null]}):null,e?(0,P.jsxs)(P.Fragment,{children:[(0,P.jsx)(d.iz,{color:"gray.200"}),(0,P.jsxs)(W,{title:"GPP Europe",children:[(0,P.jsx)(d.xv,{fontSize:"sm",fontWeight:"medium",children:"Configure TCF string for Global Privacy Platform"}),(0,P.jsx)(S.w8,{label:"Enable TC string",name:"gpp.enable_tcfeu_string",variant:"switchFirst",tooltip:"TODO"})]})]}):null]})})},Z=function(e){var r=e.children,t=e.purpose,n=e.endCol;return(0,P.jsx)(d.kC,{flex:"1",justifyContent:"center",alignItems:"center",borderLeft:"solid 1px",borderRight:n?"solid 1px":"unset",borderColor:"gray.200",height:"100%",minWidth:"36px",children:[1,3,4,5,6].includes(t)?null:(0,P.jsx)(d.xu,{children:r})})},A=function(){var e=(0,g.u6)(),r=e.values,t=e.setFieldValue,n=(0,m.C)(O.ZS).purposes;return(0,P.jsx)(g.F2,{name:"purposeOverrides",render:function(){return(0,P.jsxs)(d.kC,{flexDirection:"column",minWidth:"944px",children:[(0,P.jsxs)(d.kC,{width:"100%",border:"solid 1px",borderColor:"gray.200",backgroundColor:"gray.50",height:"36px",children:[(0,P.jsx)(d.kC,{width:"600px",pl:"4",fontSize:"xs",fontWeight:"medium",lineHeight:"4",alignItems:"center",borderRight:"solid 1px",borderColor:"gray.200",children:"TCF purpose"}),(0,P.jsx)(d.kC,{flex:"1",alignItems:"center",borderRight:"solid 1px",borderColor:"gray.200",minWidth:"36px",children:(0,P.jsx)(d.xv,{pl:"4",fontSize:"xs",fontWeight:"medium",lineHeight:"4",children:"Allowed"})}),(0,P.jsx)(d.kC,{flex:"1",alignItems:"center",borderRight:"solid 1px",borderColor:"gray.200",children:(0,P.jsx)(d.xv,{pl:"4",fontSize:"xs",fontWeight:"medium",lineHeight:"4",children:"Consent"})}),(0,P.jsx)(d.kC,{flex:"1",alignItems:"center",children:(0,P.jsx)(d.xv,{pl:"4",fontSize:"xs",fontWeight:"medium",lineHeight:"4",children:"Legitimate interest"})})]}),r.purposeOverrides.map((function(e,i){return(0,P.jsxs)(d.kC,{width:"100%",height:"36px",alignItems:"center",borderBottom:"solid 1px",borderColor:"gray.200",children:[(0,P.jsxs)(d.kC,{width:"600px",borderLeft:"solid 1px",borderColor:"gray.200",p:0,alignItems:"center",height:"100%",pl:"4",fontSize:"xs",fontWeight:"normal",lineHeight:"4",children:["Purpose ",e.purpose,": ",n[e.purpose].name]}),(0,P.jsx)(d.kC,{flex:"1",justifyContent:"center",alignItems:"center",borderLeft:"solid 1px",borderColor:"gray.200",height:"100%",children:(0,P.jsx)(d.xu,{children:(0,P.jsx)(S.w8,{name:"purposeOverrides[".concat(i,"].is_included"),onChange:function(e){e.target.checked||(t("purposeOverrides[".concat(i,"].is_consent"),!1),t("purposeOverrides[".concat(i,"].is_legitimate_interest"),!1))}})})}),(0,P.jsx)(Z,{purpose:e.purpose,children:(0,P.jsx)(S.w8,{isDisabled:!r.purposeOverrides[i].is_included||r.purposeOverrides[i].is_legitimate_interest,name:"purposeOverrides[".concat(i,"].is_consent")})}),(0,P.jsx)(Z,{purpose:e.purpose,endCol:!0,children:(0,P.jsx)(S.w8,{isDisabled:!r.purposeOverrides[i].is_included||r.purposeOverrides[i].is_consent,name:"purposeOverrides[".concat(i,"].is_legitimate_interest")})})]},e.purpose)}))]})}})},L=t(44047),N=t(51365),M=["enabled"];function H(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function q(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?H(Object(t),!0).forEach((function(r){(0,n.Z)(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):H(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}var G=function(){var e=(0,L.x8)().isLoading,r=(0,v.hz)().tcf,t=(0,L.n3)(void 0,{skip:e||!r}),n=t.data,a=t.isLoading,S=(0,L.M7)(),k=(0,c.Z)(S,1)[0],D=(0,N.tB)({api_set:!0}),T=D.data,I=D.isLoading,W=(0,N.tB)({api_set:!1}),Z=W.data,H=W.isLoading,G=(0,N.L)(),R=(0,c.Z)(G,2),V=R[0],$=R[1].isLoading,U=(0,m.C)(N.D2),B=(0,b.useMemo)((function(){return T&&null!==T&&void 0!==T&&T.consent&&"override_vendor_purposes"in T.consent?T.consent.override_vendor_purposes:!!(Z&&null!==Z&&void 0!==Z&&Z.consent&&"override_vendor_purposes"in Z.consent)&&Z.consent.override_vendor_purposes}),[T,Z]),K=(0,O.a4)().isLoading,X=(0,u.pm)(),J=function(){var e=(0,s.Z)(l().mark((function e(r){var t,n,s,c,a,u;return l().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(t=function(e){if(X.closeAll(),(0,j.D4)(e)){var r=(0,j.e$)(e.error,"An unexpected error occurred while saving. Please try again.");X((0,w.Vo)(r))}else X((0,w.t5)("Settings saved successfully"))},n=(0,o.Z)(r.purposeOverrides.map((function(e){var r;return e.is_consent&&(r=E.I$.CONSENT),e.is_legitimate_interest&&(r=E.I$.LEGITIMATE_INTERESTS),{purpose:e.purpose,is_included:e.is_included,required_legal_basis:r}}))),!B){e.next=9;break}return e.next=5,k(n);case 5:if(s=e.sent,!(0,j.D4)(s)){e.next=9;break}return t(s),e.abrupt("return");case 9:return c=r.gpp,c.enabled,a=(0,i.Z)(c,M),e.next=12,V({gpp:a});case 12:u=e.sent,t(u);case 14:case"end":return e.stop()}}),e)})));return function(r){return e.apply(this,arguments)}}(),Q=function(){var e=(0,s.Z)(l().mark((function e(r){var t,i;return l().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=function(e){if(X.closeAll(),(0,j.D4)(e)){var r=(0,j.e$)(e.error,"An unexpected error occurred while saving vendor override settings. Please try again.");X((0,w.Vo)(r))}},e.next=3,V({consent:{override_vendor_purposes:r.target.checked}});case 3:if(i=e.sent,!r.target.checked){e.next=7;break}return e.next=7,k(n.map((function(e){return q(q({},e),{},{is_included:!0,required_legal_basis:void 0})})));case 7:t(i);case 8:case"end":return e.stop()}}),e)})));return function(r){return e.apply(this,arguments)}}(),Y=(0,b.useMemo)((function(){return{purposeOverrides:n?n.map((function(e){return{purpose:e.purpose,is_included:e.is_included,is_consent:e.required_legal_basis===E.I$.CONSENT,is_legitimate_interest:e.required_legal_basis===E.I$.LEGITIMATE_INTERESTS}})):[],gpp:U}}),[n,U]);return(0,P.jsx)(y.Z,{title:"Consent Configuration",children:e||K||a||I||H?(0,P.jsx)(d.kC,{justifyContent:"center",alignItems:"center",height:"100%",children:(0,P.jsx)(p.$,{})}):(0,P.jsxs)(d.xu,{"data-testid":"consent-configuration",children:[(0,P.jsx)(d.X6,{marginBottom:4,fontSize:"2xl",children:"Consent settings"}),(0,P.jsxs)(d.Kq,{spacing:3,mb:3,children:[(0,P.jsx)(z,{title:"Transparency & Consent Framework settings",children:(0,P.jsx)(C,{name:"TCF",enabled:r})}),(0,P.jsxs)(z,{title:"Vendor overrides",children:[r?(0,P.jsxs)(P.Fragment,{children:[(0,P.jsx)(d.xv,{mb:2,fontSize:"sm",lineHeight:"5",fontWeight:"medium",color:"gray.700",children:"Configure overrides for TCF related purposes."}),(0,P.jsxs)(d.kC,{alignItems:"center",marginBottom:2,children:[(0,P.jsx)(f.r,{size:"sm",colorScheme:"purple",isChecked:B,onChange:Q,isDisabled:$}),(0,P.jsx)(d.xv,{px:2,fontSize:"sm",lineHeight:"5",fontWeight:"medium",color:"gray.700",children:"Override vendor purposes"}),(0,P.jsx)(_.Z,{label:"Toggle on if you want to globally change any flexible legal bases or remove TCF purposes from your CMP"})]}),(0,P.jsx)(d.xv,{mb:2,fontSize:"sm",lineHeight:"5",fontWeight:"medium",color:"gray.700",children:B?"The table below allows you to adjust which TCF purposes you allow as part of your user facing notices and business activites.":null})]}):null,B&&r?(0,P.jsxs)(d.xv,{fontSize:"sm",lineHeight:"5",fontWeight:"medium",color:"gray.700",children:["To configure this section, select the purposes you allow and where available, the appropriate legal bases (either Consent or Legitimate Interest)."," ",(0,P.jsxs)(x.Z,{href:"https://fid.es/tcf-overrides",children:["Read the guide on vendor overrides here."," "]})]}):null]})]}),(0,P.jsx)(g.J9,{initialValues:Y,enableReinitialize:!0,onSubmit:J,children:function(e){var r=e.dirty,t=e.isValid,n=e.isSubmitting;return(0,P.jsx)(g.l0,{children:(0,P.jsxs)(d.Kq,{spacing:6,children:[B?(0,P.jsx)(A,{}):null,(0,P.jsx)(F,{}),(0,P.jsx)(h.zx,{type:"submit",variant:"primary",size:"sm",isDisabled:!r||!t,isLoading:n,"data-testid":"save-btn",width:"fit-content",children:"Save"})]})})}})]})})}},67739:function(e,r,t){(window.__NEXT_P=window.__NEXT_P||[]).push(["/management/consent",function(){return t(39732)}])},30808:function(e,r,t){"use strict";function n(e,r){if(null==e)return{};var t,n,i={},o=Object.keys(e);for(n=0;n<o.length;n++)t=o[n],r.indexOf(t)>=0||(i[t]=e[t]);return i}t.d(r,{Z:function(){return n}})},6983:function(e,r,t){"use strict";function n(e,r){return n=Object.setPrototypeOf?Object.setPrototypeOf.bind():function(e,r){return e.__proto__=r,e},n(e,r)}t.d(r,{Z:function(){return n}})}},function(e){e.O(0,[7751,6842,3453,338,3702,9774,2888,179],(function(){return r=67739,e(e.s=r);var r}));var r=e.O();_N_E=r}]);