(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[6050],{92364:function(e,n,t){"use strict";var r=t(90849),i=t(97865),o=t(73679),s=t(29470),c=t(29549),a=t(5008),u=t(34896),l=t(9992),d=t(27378),p=t(24246);function f(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function h(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?f(Object(t),!0).forEach((function(n){(0,r.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):f(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}n.Z=function(e){var n,t=e.disabled,r=void 0!==t&&t,f=e.enableSorting,x=void 0===f||f,v=e.hasClear,j=void 0===v||v,b=e.label,m=e.list,g=e.menuButtonProps,y=e.onChange,O=e.selectedValue,C=(0,d.useState)(!1),S=C[0],w=C[1],I=function(){w(!1)},T=null===(n=(0,o.Z)(m).find((function(e){return(0,i.Z)(e,2)[1].value===O})))||void 0===n?void 0:n[0];return(0,p.jsxs)(s.v2,{isLazy:!0,onClose:I,onOpen:function(){w(!0)},strategy:"fixed",children:[(0,p.jsx)(s.j2,h(h({"aria-label":null!==T&&void 0!==T?T:b,as:c.zx,color:T?"complimentary.500":void 0,disabled:r,fontWeight:"normal",rightIcon:(0,p.jsx)(a.mC,{}),size:"sm",variant:"outline",_active:{bg:"none"},_hover:{bg:"none"}},g),{},{"data-testid":"select-dropdown-btn",children:(0,p.jsx)(u.xv,{isTruncated:!0,children:null!==T&&void 0!==T?T:b})})),S?(0,p.jsxs)(s.qy,{lineHeight:"1rem",p:"0","data-testid":"select-dropdown-list",children:[j&&(0,p.jsx)(u.kC,{borderBottom:"1px",borderColor:"gray.200",cursor:"auto",p:"8px",children:(0,p.jsx)(c.zx,{onClick:function(){y(void 0),I()},size:"xs",variant:"outline",children:"Clear"})}),(x?(0,o.Z)(m).sort():(0,o.Z)(m)).map((function(e){var n=(0,i.Z)(e,2),t=n[0],r=n[1];return(0,p.jsx)(l.u,{"aria-label":r.toolTip,hasArrow:!0,label:r.toolTip,placement:"auto-start",openDelay:500,shouldWrapChildren:!0,children:(0,p.jsx)(s.sN,{color:O===r.value?"complimentary.500":void 0,isDisabled:r.isDisabled,onClick:function(){return y(r.value)},paddingTop:"10px",paddingRight:"8.5px",paddingBottom:"10px",paddingLeft:"8.5px",_focus:{bg:"gray.100"},children:(0,p.jsx)(u.xv,{fontSize:"0.75rem",children:t})})},t)}))]}):null]})}},24753:function(e,n,t){"use strict";t.d(n,{MA:function(){return l},Vo:function(){return p},t5:function(){return d}});var r=t(90849),i=t(34896),o=t(24246);function s(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function c(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?s(Object(t),!0).forEach((function(n){(0,r.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):s(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var a=function(e){var n=e.children;return(0,o.jsxs)(i.xv,{"data-testid":"toast-success-msg",children:[(0,o.jsx)("strong",{children:"Success:"})," ",n]})},u=function(e){var n=e.children;return(0,o.jsxs)(i.xv,{"data-testid":"toast-error-msg",children:[(0,o.jsx)("strong",{children:"Error:"})," ",n]})},l={variant:"subtle",position:"top",description:"",duration:5e3,status:"success",isClosable:!0},d=function(e){var n=(0,o.jsx)(a,{children:e});return c(c({},l),{description:n})},p=function(e){var n=(0,o.jsx)(u,{children:e});return c(c({},l),{description:n,status:"error"})}},79375:function(e,n,t){"use strict";t.r(n),t.d(n,{default:function(){return z}});var r=t(34896),i=t(64289),o=t(43890),s=t(86677),c=t(27378),a=t(60245),u=t(6848),l=t(56069),d=t(60709),p=t(73679),f=t(32751),h=t(5008),x=t(29549),v=t(83125),j=t(1326),b=t(63238),m=t(92213),g=t(9865),y=t(92364),O=t(13717),C=t(24246),S=function(e){var n=e.width,t=(0,a.I0)(),o=(0,c.useRef)(!1),s=(0,u.C)(i.pw);return(0,c.useEffect)((function(){return o.current=!0,function(){t((0,i.zq)(O.gA)),o.current=!1}}),[t]),(0,C.jsx)(r.xu,{children:(0,C.jsx)(y.Z,{enableSorting:!1,hasClear:!1,label:"Show all connectors",list:O.yI,menuButtonProps:{width:n},onChange:function(e){t((0,i.zq)(e||O.gA))},selectedValue:s.system_type||O.gA})})},w=t(79894),I=t.n(w),T=function(e){var n=e.items;return(0,C.jsx)(r.MI,{columns:4,spacingX:"16px",spacingY:"16px",children:n.map((function(e){return(0,C.jsx)(I(),{href:{pathname:window.location.pathname,query:{step:2,connectorType:JSON.stringify(e)}},passHref:!0,children:(0,C.jsx)(r.xu,{boxShadow:"base",borderRadius:"5px",maxWidth:"331px",overflow:"hidden",_hover:{boxShadow:"lg",cursor:"pointer"},"data-testid":"".concat(e.identifier,"-item"),children:(0,C.jsxs)(r.kC,{alignItems:"center",justifyContent:"start",pl:"24px",pr:"24px",color:"gray.700",fontSize:"14px",fontStyle:"normal",fontWeight:"600",lineHeight:"20px",h:"80px",children:[(0,C.jsx)(o.Z,{data:e}),(0,C.jsx)(r.xv,{ml:"12px",children:e.human_readable})]})})},e.identifier)}))})},E=function(){var e=(0,a.I0)(),n=(0,c.useRef)(!1),t=(0,u.C)(i.ZZ).step,o=(0,u.C)(i.pw),s=(0,i.$I)(o),l=s.data,d=s.isFetching,y=s.isLoading,O=s.isSuccess,w=(0,c.useState)(!1),I=w[0],E=w[1],Z=(0,c.useCallback)((function(n){(0===n.target.value.length||n.target.value.length>1)&&e((0,i.qP)(n.target.value))}),[e]),_=(0,c.useMemo)((function(){return(0,j.Ds)(Z,250)}),[Z]),k=(0,c.useMemo)((function(){return(null===l||void 0===l?void 0:l.items)&&(0,p.Z)(l.items).sort((function(e,n){return e.human_readable>n.human_readable?1:-1}))}),[l]);return(0,c.useEffect)((function(){return n.current=!0,function(){e((0,i.qP)("")),n.current=!1}}),[e]),(0,C.jsxs)(C.Fragment,{children:[(0,C.jsx)(r.kC,{minWidth:"fit-content",children:(0,C.jsx)(r.xu,{color:"gray.700",fontSize:"14px",maxHeight:"80px",maxWidth:"474px",mb:"24px",children:t.description})}),(0,C.jsxs)(r.kC,{alignItems:"center",gap:"4",mb:"24px",minWidth:"fit-content",children:[(0,C.jsx)(S,{}),(0,C.jsxs)(f.BZ,{size:"sm",children:[(0,C.jsx)(f.Z8,{pointerEvents:"none",children:(0,C.jsx)(h.PT,{color:"gray.300",h:"17px",w:"17px"})}),(0,C.jsx)(f.II,{autoComplete:"off",autoFocus:!0,borderRadius:"md",name:"search",onChange:_,placeholder:"Search integrations",size:"sm",type:"search"})]}),(0,C.jsx)(b.ZP,{scopes:[g.Sh.CONNECTOR_TEMPLATE_REGISTER],children:(0,C.jsx)(x.zx,{colorScheme:"primary",type:"submit",minWidth:"auto","data-testid":"upload-btn",size:"sm",onClick:function(){E(!0)},children:"Upload connector"})})]}),(0,C.jsx)(m.Z,{isOpen:I,onClose:function(){return E(!1)}}),(d||y)&&(0,C.jsx)(r.M5,{children:(0,C.jsx)(v.$,{})}),O&&k?(0,C.jsx)(T,{items:k}):null]})},Z=t(44204),_=t(39100),k=t(53771),P=t(53552),A=function(){var e=(0,a.I0)(),n=(0,c.useRef)(!1),t=(0,c.useState)(!1),o=t[0],s=t[1],l=(0,u.C)(i.ZZ),d=l.connection,p=l.connectionOption,f=O.IM.find((function(e){return e.type===(null===p||void 0===p?void 0:p.type)})),h=(0,c.useState)(null===f||void 0===f?void 0:f.options[0]),x=h[0],v=h[1],j=function(){s(!0)},b=(0,c.useMemo)((function(){return function(){var e=[];return null!==f&&void 0!==f&&f.options&&f.options.forEach((function(n){var t;switch(n){case O.H5.CONNECTOR_PARAMETERS:t={label:n,content:(0,C.jsx)(_.s,{onConnectionCreated:j})};break;case O.H5.DATASET_CONFIGURATION:t=null!==d&&void 0!==d&&d.key?{label:n,content:(0,C.jsx)(k.Z,{})}:void 0;break;case O.H5.DSR_CUSTOMIZATION:t=null!==d&&void 0!==d&&d.key?{label:n,content:(0,C.jsx)(P.Z,{})}:void 0}t&&e.push(t)})),e}}),[null===d||void 0===d?void 0:d.key,null===f||void 0===f?void 0:f.options]),m=(0,c.useCallback)((function(n){switch(n){case O.H5.DATASET_CONFIGURATION:case O.H5.DSR_CUSTOMIZATION:e((0,i.nj)(O.Ss[3]));break;case O.H5.CONNECTOR_PARAMETERS:default:e((0,i.nj)(O.Ss[2]))}v(n)}),[e]);return(0,c.useEffect)((function(){return n.current=!0,function(){n.current=!1,e((0,i.mc)())}}),[e]),(0,c.useEffect)((function(){null!==d&&void 0!==d&&d.key&&(m((null===p||void 0===p?void 0:p.type)!==g.Zi.MANUAL?O.H5.DATASET_CONFIGURATION:O.H5.DSR_CUSTOMIZATION),o&&s(!1))}),[o,null===d||void 0===d?void 0:d.key,null===p||void 0===p?void 0:p.type,null===f||void 0===f?void 0:f.options,m]),(0,C.jsx)(r.gC,{alignItems:"stretch",gap:"18px",children:(0,C.jsx)(Z.Z,{data:b(),flexGrow:1,index:null===f||void 0===f?void 0:f.options.findIndex((function(e){return e===x})),isLazy:!0})})},N=t(60933),R=function(){var e=(0,a.I0)(),n=(0,s.useRouter)(),t=n.query,p=t.connectorType,f=t.step,h=(0,u.C)(i.ZZ),x=h.connection,v=h.connectionOption,j=h.step;(0,c.useEffect)((function(){if(p&&e((0,i.yA)(JSON.parse(p))),n.query.step){var t=O.Ss.find((function(e){return e.stepId===Number(f)}));e((0,i.nj)(t||O.Ss[1]))}return!n.query.id&&null!==x&&void 0!==x&&x.key&&(0,N.S)(x.key,j.href),function(){}}),[null===x||void 0===x?void 0:x.key,p,f,e,n.query.id,n.query.step,j.href]);var b=(0,c.useCallback)((function(e){var n="";switch(e.stepId){case 2:case 3:n=e.label.replace("{identifier}",v.human_readable);break;default:n=e.label}return n}),[v]);return(0,C.jsxs)(C.Fragment,{children:[(0,C.jsx)(l.Z,{backPath:d.JR}),(0,C.jsx)(r.X6,{fontSize:"2xl",fontWeight:"semibold",maxHeight:"40px",mb:"4px",whiteSpace:"nowrap",children:(0,C.jsxs)(r.xu,{alignItems:"center",display:"flex",children:[v&&(0,C.jsxs)(C.Fragment,{children:[(0,C.jsx)(o.Z,{data:v}),(0,C.jsx)(r.xv,{ml:"8px",children:b(j)})]}),!v&&(0,C.jsx)(r.xv,{children:b(j)})]})}),function(){switch(j.stepId){case 1:default:return(0,C.jsx)(E,{});case 2:case 3:return(0,C.jsx)(A,{})}}()]})},D=t(66156),z=function(){return(0,C.jsx)(D.Z,{children:(0,C.jsx)(R,{})})}},91747:function(e,n,t){(window.__NEXT_P=window.__NEXT_P||[]).push(["/datastore-connection/new",function(){return t(79375)}])}},function(e){e.O(0,[7751,530,6842,3452,3453,8301,6155,9198,7068,4833,7232,338,3702,8148,6286,9774,2888,179],(function(){return n=91747,e(e.s=n);var n}));var n=e.O();_N_E=n}]);