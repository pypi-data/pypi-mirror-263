(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[4202],{2424:function(e,n,t){"use strict";var r=t(90849),i=t(90089),a=t(30794),o=t(24246),s=["name","onClose"];function l(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function u(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?l(Object(t),!0).forEach((function(n){(0,r.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):l(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}n.Z=function(e){var n=e.name,t=e.onClose,r=(0,i.Z)(e,s),l=u({backgroundColor:"primary.400",color:"white","data-testid":"taxonomy-entity-".concat(n),width:"fit-content",size:"sm"},r);return t?(0,o.jsxs)(a.Vp,u(u({display:"flex",justifyContent:"space-between"},l),{},{children:[(0,o.jsx)(a.Sn,{children:n}),(0,o.jsx)(a.SD,{onClick:t,color:"white"})]})):(0,o.jsx)(a.Vp,u(u({},l),{},{children:n}))}},64929:function(e,n,t){"use strict";t.d(n,{C:function(){return r},P:function(){return i}});var r=function e(n,t){var r;if(null==t&&n.every((function(e){return void 0===e.parent_key})))r=n;else{var i=null!==t&&void 0!==t?t:null;r=n.filter((function(e){return e.parent_key===i}))}return r.map((function(t){var r,i,a=t.fides_key;return{value:t.fides_key,label:""===t.name||null==t.name?t.fides_key:t.name,description:t.description,children:e(n,a),is_default:null!==(r=t.is_default)&&void 0!==r&&r,active:null!==(i=t.active)&&void 0!==i&&i}}))},i=function(e){var n=e.split(".");return 1===n.length?"":n.slice(0,n.length-1).join(".")}},53136:function(e,n,t){"use strict";t.r(n),t.d(n,{default:function(){return ne}});var r=t(34896),i=t(51471),a=t(29549),o=t(6848),s=t(44204),l=t(55732),u=t(97865),c=t(90849),d=t(34707),f=t.n(d),p=t(27378),y=t(14275),v=t(1261),x=t(9865),h=[{label:"Yes",value:"true"},{label:"No",value:"false"}],m=t(43139),b=t(78624),j=t(47134),g=t(75846),_=t(64929),k=t(10612),E=t(24246);function w(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function O(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?w(Object(t),!0).forEach((function(n){(0,c.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):w(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var C=function(e,n){var t,r,i,a,o,s,l,u;return{fides_key:null!==(t=e.fides_key)&&void 0!==t?t:"",name:null!==(r=e.name)&&void 0!==r?r:"",description:null!==(i=e.description)&&void 0!==i?i:"",parent_key:null!==(a=e.parent_key)&&void 0!==a?a:"",is_default:null!==(o=e.is_default)&&void 0!==o&&o,version_added:null!==(s=e.version_added)&&void 0!==s?s:void 0,version_deprecated:null!==(l=e.version_deprecated)&&void 0!==l?l:void 0,replaced_by:null!==(u=e.replaced_by)&&void 0!==u?u:void 0,customFieldValues:n}},T=function(e,n){var t=""===e.fides_key,r=O({},n);if(t){var i=(0,_.P)(n.fides_key);r.parent_key=""===i?void 0:i}else r.parent_key=""===e.parent_key?void 0:e.parent_key,r.fides_key=e.fides_key;return delete r.customFieldValues,r},D=t(30794),F=t(21084),P=t(70409),S=t(83125),Z=t(62332);function z(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function V(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?z(Object(t),!0).forEach((function(n){(0,c.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):z(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var K=function(e){var n=e.nodes,t=e.focusedKey,i=e.renderHover,a=e.renderTag,o=(0,p.useState)(void 0),s=o[0],l=o[1],u=function e(n){var o=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0,u=(null===s||void 0===s?void 0:s.value)===n.value,c=t===n.value,d={borderBottom:"1px solid",borderColor:"gray.200",display:"flex",justifyContent:"space-between",alignItems:"center",pl:3*o,_hover:{bg:"gray.50"},onMouseEnter:function(){l(n)},onMouseLeave:function(){l(void 0)}},f=u&&i?i(n):null;return 0===n.children.length?(0,E.jsxs)(r.xu,V(V({py:2},d),{},{children:[(0,E.jsxs)(r.xu,{display:"flex",alignItems:"center",children:[(0,E.jsx)(r.xv,{"data-testid":"item-".concat(n.label),pl:5,color:c?"complimentary.500":void 0,mr:2,children:n.label}),a?a(n):null]}),f]})):(0,E.jsxs)(Z.Qd,{p:0,border:"none",children:[(0,E.jsxs)(r.xu,V(V({},d),{},{children:[(0,E.jsxs)(Z.KF,{_expanded:{color:"complimentary.500"},_hover:{bg:"gray.50"},pl:0,color:c?"complimentary.500":void 0,children:[(0,E.jsx)(Z.XE,{}),(0,E.jsx)(r.xv,{"data-testid":"accordion-item-".concat(n.label),mr:2,children:n.label}),a?a(n):null]}),f]})),(0,E.jsx)(Z.Hk,{p:0,children:n.children.map((function(n){return(0,E.jsx)(p.Fragment,{children:e(n,o+1)},n.value)}))})]})};return(0,E.jsx)(r.xu,{boxSizing:"border-box",children:(0,E.jsx)(Z.UQ,{allowMultiple:!0,children:n.map((function(e){return(0,E.jsx)(r.xu,{children:u(e)},e.value)}))})})},M=t(2458),A=t(24753),L=t(33167),U=t(73452),I=t(62709),X=function(e){var n=e.node,t=e.onEdit,i=e.onDelete,o=e.onDisable,s=!n.is_default;return(0,E.jsxs)(r.Ug,{mr:4,children:[(0,E.jsxs)(a.hE,{size:"xs",variant:"outline",colorScheme:"gray","data-testid":"action-btns",children:[(0,E.jsx)(a.hU,{"aria-label":"Edit",icon:(0,E.jsx)(U.dY,{boxSize:3}),onClick:function(){return t(n)},"data-testid":"edit-btn"}),s?(0,E.jsx)(a.hU,{"aria-label":"Delete",icon:(0,E.jsx)(U.pJ,{boxSize:3}),onClick:function(){return i(n)},"data-testid":"delete-btn"}):null]}),(0,E.jsx)(I.r,{size:"sm",colorScheme:"purple",defaultChecked:n.active,onChange:function(){return o(n)}}),(0,E.jsx)(r.xv,{children:"Enabled"})]})},q=t(92975),R=t(32751),G=t(34090),N=t(68301),Y=t(2424),B=function(e){var n=e.labels,t=e.onCancel,i=e.onSubmit,o=e.renderExtraFormFields,s=e.initialValues,u=(0,P.pm)(),c=(0,p.useState)(null),d=c[0],y=c[1],v=N.Ry().shape({fides_key:N.Z_().required().label(n.fides_key)}),x=""===s.fides_key,h=function(e){var n=(0,b.nU)(e);y(n.message)},j=function(){var e=(0,l.Z)(f().mark((function e(n){var r;return f().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return y(null),e.next=3,i(s,n);case 3:r=e.sent,(0,b.D4)(r)?h(r.error):(u((0,A.t5)("Taxonomy successfully ".concat(x?"created":"updated"))),x&&t());case 5:case"end":return e.stop()}}),e)})));return function(n){return e.apply(this,arguments)}}();return(0,E.jsxs)(r.Kq,{pl:6,spacing:6,"data-testid":"".concat(x?"create":"edit","-taxonomy-form"),children:[(0,E.jsxs)(r.X6,{size:"md",textTransform:"capitalize","data-testid":"form-heading",children:[x?"Create":"Modify"," ",n.fides_key]}),(0,E.jsx)(G.J9,{initialValues:s,onSubmit:j,validationSchema:v,enableReinitialize:!0,children:function(e){var i=e.dirty,l=e.values;return(0,E.jsxs)(G.l0,{children:[(0,E.jsxs)(r.Kq,{mb:6,children:[x?(0,E.jsx)(m.j0,{name:"fides_key",label:n.fides_key}):(0,E.jsxs)(r.rj,{templateColumns:"1fr 3fr",children:[(0,E.jsx)(q.lX,{children:n.fides_key}),(0,E.jsx)(r.xu,{children:(0,E.jsx)(Y.Z,{name:s.fides_key})})]}),(0,E.jsx)(m.j0,{name:"name",label:n.name}),(0,E.jsx)(m.Ks,{name:"description",label:n.description}),n.parent_key&&(x?(0,E.jsxs)(r.rj,{templateColumns:"1fr 3fr",children:[(0,E.jsx)(q.lX,{children:n.parent_key}),(0,E.jsx)(r.xu,{mr:"2",children:(0,E.jsx)(R.II,{"data-testid":"input-parent_key",disabled:!0,value:(0,_.P)(l.fides_key),size:"sm"})})]}):(0,E.jsx)(m.j0,{name:"parent_key",label:n.parent_key,disabled:!x})),o?o(l):null]}),d?(0,E.jsx)(r.xv,{color:"red",mb:2,"data-testid":"taxonomy-form-error",children:d}):null,(0,E.jsxs)(a.hE,{size:"sm",children:[(0,E.jsx)(a.zx,{"data-testid":"cancel-btn",variant:"outline",onClick:t,children:"Cancel"}),(0,E.jsx)(a.zx,{"data-testid":"submit-btn",variant:"primary",type:"submit",disabled:!x&&!i,children:x?"Create entity":"Update entity"})]})]})}})]})},W=function(e){var n=e.node;return n.is_default?null:(0,E.jsx)(D.Vp,{backgroundColor:"purple.500",color:"white",size:"sm",height:"fit-content","data-testid":"custom-tag-".concat(n.label),children:"CUSTOM"})},H=function(e){var n=e.node;return n.active?null:(0,E.jsx)(D.Vp,{backgroundColor:"gray.500",color:"white",size:"sm",height:"fit-content","data-testid":"custom-tag-".concat(n.label),children:"DISABLED"})},J={fides_key:"",parent_key:"",name:"",description:""},Q=function(e){var n=e.useTaxonomy,t=(0,o.T)(),i=n(),a=i.isLoading,s=i.data,u=i.labels,c=i.entityToEdit,d=i.setEntityToEdit,y=i.handleCreate,v=i.handleEdit,x=i.handleDelete,h=i.handleToggleEnabled,m=i.renderExtraFormFields,j=i.transformEntityToInitialValues,g=(0,p.useMemo)((function(){return s?(0,_.C)(s):null}),[s]),w=(0,p.useState)(null),O=w[0],C=w[1],T=(0,p.useState)(null),D=T[0],Z=T[1],z=(0,o.C)(k.yK);(0,p.useEffect)((function(){z&&d(null)}),[z,d]);var V=function(){t((0,k.Gz)(!1))},U=(0,F.qY)(),I=U.isOpen,q=U.onOpen,R=U.onClose,G=(0,F.qY)(),N=G.isOpen,Y=G.onOpen,Q=G.onClose,$=(0,P.pm)();if(a)return(0,E.jsx)(r.M5,{children:(0,E.jsx)(S.$,{})});if(!g)return(0,E.jsx)(r.xv,{children:"Could not find data."});var ee=u.fides_key.toLocaleLowerCase(),ne=function(e){var n;z&&V();var t=null!==(n=null===s||void 0===s?void 0:s.find((function(n){return n.fides_key===e.value})))&&void 0!==n?n:null;d(t)},te=function(e){C(e),q()},re=function(e){Z(e),Y()},ie=function(){var e=(0,l.Z)(f().mark((function e(){var n;return f().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!O){e.next=7;break}return e.next=3,x(O.value);case 3:n=e.sent,(0,L.isErrorResult)(n)?$((0,A.Vo)((0,b.e$)(n.error))):$((0,A.t5)("Successfully deleted ".concat(ee))),R(),d(null);case 7:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),ae=function(){var e=(0,l.Z)(f().mark((function e(){var n,t,r,i;return f().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!(t=null!==(n=D&&(null===s||void 0===s?void 0:s.find((function(e){return e.fides_key===D.value}))))&&void 0!==n?n:null)){e.next=9;break}return r=null===D||void 0===D?void 0:D.active,e.next=5,h(t,!r);case 5:i=e.sent,(0,L.isErrorResult)(i)?$((0,A.Vo)((0,b.e$)(i.error))):$((0,A.t5)("Successfully ".concat(r?"disabled":"enabled"," ").concat(ee))),Q(),d(null);case 9:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}();return(0,E.jsxs)(E.Fragment,{children:[(0,E.jsxs)(r.MI,{columns:2,spacing:2,children:[(0,E.jsx)(K,{nodes:g,focusedKey:null===c||void 0===c?void 0:c.fides_key,renderHover:function(e){return(0,E.jsx)(X,{onDelete:te,onEdit:ne,onDisable:re,node:e})},renderTag:function(e){return(0,E.jsxs)(r.Ug,{spacing:2,children:[(0,E.jsx)(W,{node:e}),(0,E.jsx)(H,{node:e})]})}}),c?(0,E.jsx)(B,{labels:u,onCancel:function(){return d(null)},onSubmit:v,renderExtraFormFields:m,initialValues:j(c)}):null,z?(0,E.jsx)(B,{labels:u,onCancel:V,onSubmit:y,renderExtraFormFields:m,initialValues:j(J)}):null]}),O?(0,E.jsx)(M.Z,{isOpen:I,onClose:R,onConfirm:ie,title:"Delete ".concat(ee),message:(0,E.jsxs)(r.Kq,{children:[(0,E.jsxs)(r.xv,{children:["You are about to permanently delete the ",ee," ",(0,E.jsx)(r.xv,{color:"complimentary.500",as:"span",fontWeight:"bold",children:O.value})," ","from your taxonomy. Are you sure you would like to continue?"]}),O.children.length?(0,E.jsxs)(r.xv,{color:"red","data-testid":"delete-children-warning",children:["Deleting"," ",(0,E.jsx)(r.xv,{as:"span",fontWeight:"bold",children:O.value})," ","will also delete all of its children."]}):null]})}):null,D?(0,E.jsx)(M.Z,{isOpen:N,onClose:Q,onConfirm:ae,title:"".concat(D.active?"Disable":"Enable"," ").concat(ee),message:(0,E.jsx)(r.Kq,{children:(0,E.jsxs)(r.xv,{children:["This will ",D.active?"disable":"enable"," ","the ",ee," ",(0,E.jsx)(r.xv,{color:"complimentary.500",as:"span",fontWeight:"bold",children:D.value})," ","from your taxonomy."]})})}):null]})},$=[{label:"Data Categories",content:(0,E.jsx)(Q,{useTaxonomy:function(){var e=x.P6.DATA_CATEGORY,n=(0,p.useState)(null),t=n[0],r=n[1],i=(0,k.MO)(),a=i.data,o=i.isLoading,s=(0,k.Ti)(),c=(0,u.Z)(s,1)[0],d=(0,k.jU)(),h=(0,u.Z)(d,1)[0],m=(0,k.K9)(),b=(0,u.Z)(m,1)[0],j=(0,v.m)({resourceFidesKey:null===t||void 0===t?void 0:t.fides_key,resourceType:e}),g=function(){var e=(0,l.Z)(f().mark((function e(n,t){var r,i;return f().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return r=T(n,t),e.next=3,c(r);case 3:if(i=e.sent,!j.isEnabled){e.next=7;break}return e.next=7,j.upsertCustomFields(t);case 7:return e.abrupt("return",i);case 8:case"end":return e.stop()}}),e)})));return function(n,t){return e.apply(this,arguments)}}(),_=function(){var e=(0,l.Z)(f().mark((function e(n,t){var r,i;return f().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(r=T(n,t),i=h(r),!j.isEnabled){e.next=5;break}return e.next=5,j.upsertCustomFields(t);case 5:return e.abrupt("return",i);case 6:case"end":return e.stop()}}),e)})));return function(n,t){return e.apply(this,arguments)}}(),w=b,D=function(){var e=(0,l.Z)(f().mark((function e(n,t){var r,i;return f().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return r=O(O({},n),{},{active:t}),i=h(r),e.abrupt("return",i);case 3:case"end":return e.stop()}}),e)})));return function(n,t){return e.apply(this,arguments)}}();return{data:a,isLoading:o,labels:{fides_key:"Data category",name:"Category name",description:"Category description",parent_key:"Parent category"},resourceType:e,entityToEdit:t,setEntityToEdit:r,handleCreate:g,handleEdit:_,handleDelete:w,handleToggleEnabled:D,renderExtraFormFields:function(n){return(0,E.jsx)(y.uc,{resourceFidesKey:n.fides_key,resourceType:e})},transformEntityToInitialValues:function(e){return C(e,j.customFieldValues)}}}})},{label:"Data Uses",content:(0,E.jsx)(Q,{useTaxonomy:function(){var e=x.P6.DATA_USE,n=(0,p.useState)(null),t=n[0],r=n[1],i=(0,g.fd)(),a=i.data,o=i.isLoading,s=(0,g.Ql)(),c=(0,u.Z)(s,1)[0],d=(0,g.LG)(),h=(0,u.Z)(d,1)[0],m=(0,g.gu)(),b=(0,u.Z)(m,1)[0],j=function(e){return O({},e)},_=(0,v.m)({resourceFidesKey:null===t||void 0===t?void 0:t.fides_key,resourceType:e}),k=function(){var e=(0,l.Z)(f().mark((function e(n,t){var r,i;return f().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return r=j(T(n,t)),e.next=3,c(r);case 3:if(i=e.sent,!_.isEnabled){e.next=7;break}return e.next=7,_.upsertCustomFields(t);case 7:return e.abrupt("return",i);case 8:case"end":return e.stop()}}),e)})));return function(n,t){return e.apply(this,arguments)}}(),w=function(){var e=(0,l.Z)(f().mark((function e(n,t){var r,i;return f().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(r=j(T(n,t)),i=h(r),!_.isEnabled){e.next=5;break}return e.next=5,_.upsertCustomFields(t);case 5:return e.abrupt("return",i);case 6:case"end":return e.stop()}}),e)})));return function(n,t){return e.apply(this,arguments)}}(),D=b,F=function(){var e=(0,l.Z)(f().mark((function e(n,t){var r,i;return f().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(r=O(O({},n),{},{active:t}),i=h(r),!_.isEnabled){e.next=5;break}return e.next=5,_.upsertCustomFields(r);case 5:return e.abrupt("return",i);case 6:case"end":return e.stop()}}),e)})));return function(n,t){return e.apply(this,arguments)}}();return{data:a,isLoading:o,labels:{fides_key:"Data use",name:"Data use name",description:"Data use description",parent_key:"Parent data use"},resourceType:e,entityToEdit:t,setEntityToEdit:r,handleCreate:k,handleEdit:w,handleDelete:D,handleToggleEnabled:F,renderExtraFormFields:function(n){return(0,E.jsx)(y.uc,{resourceFidesKey:n.fides_key,resourceType:e})},transformEntityToInitialValues:function(e){return O({},C(e,_.customFieldValues))}}}})},{label:"Data Subjects",content:(0,E.jsx)(Q,{useTaxonomy:function(){var e=x.P6.DATA_SUBJECT,n=(0,p.useState)(null),t=n[0],r=n[1],i=(0,j.te)(),a=i.data,o=i.isLoading,s={fides_key:"Data subject",name:"Data subject name",description:"Data subject description",rights:"Rights",strategy:"Strategy",automatic_decisions:"Automatic decisions or profiling"},c=(0,j.wG)(),d=(0,u.Z)(c,1)[0],g=(0,j.h8)(),_=(0,u.Z)(g,1)[0],k=(0,j.Kv)(),w=(0,u.Z)(k,1)[0],D=function(e){var n,t=O(O({},e),{},{rights:e.rights.length?{values:e.rights,strategy:e.strategy}:void 0,automatic_decisions_or_profiling:!("true"!==(null===(n=e.automated_decisions_or_profiling)||void 0===n?void 0:n.toString()))});return delete t.strategy,t},F=(0,v.m)({resourceFidesKey:null===t||void 0===t?void 0:t.fides_key,resourceType:e}),P=function(){var e=(0,l.Z)(f().mark((function e(n,t){var r,i;return f().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return r=D(T(n,t)),e.next=3,d(r);case 3:if(i=e.sent,!F.isEnabled){e.next=7;break}return e.next=7,F.upsertCustomFields(t);case 7:return e.abrupt("return",i);case 8:case"end":return e.stop()}}),e)})));return function(n,t){return e.apply(this,arguments)}}(),S=function(){var e=(0,l.Z)(f().mark((function e(n,t){var r,i;return f().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(r=D(T(n,t)),i=_(r),!F.isEnabled){e.next=5;break}return e.next=5,F.upsertCustomFields(t);case 5:return e.abrupt("return",i);case 6:case"end":return e.stop()}}),e)})));return function(n,t){return e.apply(this,arguments)}}(),Z=w,z=function(){var e=(0,l.Z)(f().mark((function e(n,t){var r,i;return f().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(r=O(O({},n),{},{active:t}),i=_(r),!F.isEnabled){e.next=5;break}return e.next=5,F.upsertCustomFields(r);case 5:return e.abrupt("return",i);case 6:case"end":return e.stop()}}),e)})));return function(n,t){return e.apply(this,arguments)}}();return{data:a,isLoading:o,labels:s,resourceType:e,entityToEdit:t,setEntityToEdit:r,handleCreate:P,handleEdit:S,handleDelete:Z,handleToggleEnabled:z,renderExtraFormFields:function(n){return(0,E.jsxs)(E.Fragment,{children:[(0,E.jsx)(m.AP,{name:"rights",label:s.rights,options:(0,b.MM)(x.ts),isMulti:!0}),n.rights&&n.rights.length?(0,E.jsx)(m.AP,{name:"strategy",label:s.strategy,options:(0,b.MM)(x.jX)}):null,(0,E.jsx)(m.xt,{name:"automatic_decisions_or_profiling",label:s.automatic_decisions,options:h}),(0,E.jsx)(y.uc,{resourceFidesKey:n.fides_key,resourceType:e})]})},transformEntityToInitialValues:function(e){var n,t,r;return O(O({},C(e,F.customFieldValues)),{},{rights:null!==(n=null===(t=e.rights)||void 0===t?void 0:t.values)&&void 0!==n?n:[],strategy:null===(r=e.rights)||void 0===r?void 0:r.strategy,automatic_decisions_or_profiling:null==e.automated_decisions_or_profiling?"false":e.automated_decisions_or_profiling.toString()})}}}})}],ee=function(){var e=(0,o.T)();return(0,E.jsxs)(r.xu,{"data-testid":"taxonomy-tabs",display:"flex",children:[(0,E.jsx)(s.Z,{border:"full-width",data:$,flexGrow:1,isLazy:!0}),(0,E.jsx)(r.xu,{borderBottom:"2px solid",borderColor:"gray.200",height:"fit-content",pr:"2",pb:"2",children:(0,E.jsx)(a.zx,{size:"sm",variant:"outline",onClick:function(){e((0,k.Gz)(!0))},"data-testid":"add-taxonomy-btn",children:"Add Taxonomy Entity +"})})]})},ne=function(){return(0,E.jsxs)(i.Z,{title:"Datasets",children:[(0,E.jsx)(r.X6,{mb:2,fontSize:"2xl",fontWeight:"semibold",children:"Taxonomy Management"}),(0,E.jsx)(ee,{})]})}},33167:function(e,n,t){"use strict";t.d(n,{isAPIError:function(){return r.Bw},isErrorResult:function(){return r.D4}});var r=t(60041)},71180:function(e,n,t){(window.__NEXT_P=window.__NEXT_P||[]).push(["/taxonomy",function(){return t(53136)}])}},function(e){e.O(0,[7751,530,6842,3452,3453,8301,6155,4196,338,3702,3119,9774,2888,179],(function(){return n=71180,e(e.s=n);var n}));var n=e.O();_N_E=n}]);