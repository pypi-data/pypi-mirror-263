(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[3685],{85375:function(e,t,r){"use strict";var n=r(90849),i=r(73679),o=r(73452),s=r(34896),c=r(29549),u=r(58981),l=r(60153),a=r(89871),d=r(58897),p=r(27378),f=r(43139),x=r(38687),b=r(24246);function j(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function v(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?j(Object(r),!0).forEach((function(t){(0,n.Z)(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):j(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}var h=function(e){var t=e.item,r=e.label,n=e.draggable,i=e.onDeleteItem,u=e.onRowClick,d=e.maxH,p=void 0===d?10:d,f=(0,l.o)();return(0,b.jsx)(a.t.Item,{value:t,dragListener:!1,dragControls:f,children:(0,b.jsxs)(s.kC,{direction:"row",gap:2,maxH:p,w:"full",px:2,align:"center",role:"group",borderY:"1px",my:"-1px",borderColor:"gray.200",_hover:u?{bgColor:"gray.100"}:void 0,bgColor:"white",children:[n?(0,b.jsx)(o.VV,{onPointerDown:function(e){return f.start(e)},cursor:"grab"}):null,(0,b.jsx)(s.kC,{direction:"row",gap:2,p:2,align:"center",w:"full",cursor:u?"pointer":"auto",onClick:function(){u&&u(t)},overflow:"clip",children:(0,b.jsx)(s.xv,{fontSize:"sm",userSelect:"none",textOverflow:"ellipsis",whiteSpace:"nowrap",overflow:"hidden",children:r})}),i?(0,b.jsx)(c.hU,{"aria-label":"Delete",onClick:function(){return i(t)},icon:(0,b.jsx)(o.pJ,{}),size:"xs",variant:"outline",bgColor:"white",visibility:"hidden",alignSelf:"end",mb:2,_groupHover:{visibility:"visible"}}):null]})})},m=function(e){var t=e.label,r=e.options,n=e.onOptionSelected,i=(0,p.useState)(!1),l=i[0],a=i[1],d=(0,p.useState)(void 0),x=d[0],j=d[1];return l?(0,b.jsx)(s.xu,{w:"full",children:(0,b.jsx)(u.Z,{chakraStyles:f.hP,size:"sm",value:x,options:r,onChange:function(e){return n(e),a(!1),void j(void 0)},autoFocus:!0,menuPosition:"fixed",menuPlacement:"auto"})}):(0,b.jsx)(c.zx,{onClick:function(){return a(!0)},w:"full",size:"sm",variant:"outline",rightIcon:(0,b.jsx)(o.dt,{boxSize:3}),children:t})};t.Z=function(e){var t=e.label,r=e.tooltip,n=e.draggable,o=e.addButtonLabel,c=e.allItems,u=e.idField,l=e.nameField,p=void 0===l?u:l,j=e.values,y=e.setValues,g=e.canDeleteItem,O=e.onRowClick,w=e.selectOnAdd,P=e.getItemLabel,S=e.createNewValue,C=e.maxHeight,k=void 0===C?36:C,D=function(e){return e instanceof Object&&u&&u in e?e[u]:e},Z=c.every((function(e){return"string"===typeof e}))?c.filter((function(e){return j.every((function(t){return t!==e}))})):c.filter((function(e){return j.every((function(t){return D(t)!==D(e)}))})),_=function(e){y(j.filter((function(t){return t!==e})).slice())},E=null!==P&&void 0!==P?P:function(e){return e instanceof Object&&u&&u in e?p&&p in e?e[p]:e[u]:e},z=function(e){var t=e instanceof Object&&u&&u in e?e[u]:e;return{label:E(e),value:t}},I=function(e){var t=S?S(e):function(e){return c.every((function(e){return"string"===typeof e}))?e.value:c.find((function(t){return t[u]===e.value}))}(e);y([t].concat((0,i.Z)(j.slice()))),w&&O&&O(t)},R={border:"1px",borderColor:"gray.200",borderRadius:"md",w:"full",maxH:"8.5rem",overflowY:"auto"},A=n?(0,b.jsx)(s.xu,v(v({as:d.E.div,layoutScroll:!0},R),{},{children:(0,b.jsx)(a.t.Group,{values:j,onReorder:function(e){return y(e.slice())},children:j.map((function(e){return(0,b.jsx)(h,{item:e,label:E(e),onDeleteItem:!g||g&&g(e)?_:void 0,onRowClick:O,draggable:!0,maxH:k},D(e))}))})})):(0,b.jsx)(s.xu,v(v({},R),{},{children:(0,b.jsx)(s.aV,{children:j.map((function(e){return(0,b.jsx)(h,{item:e,label:E(e),onRowClick:O,onDeleteItem:_,maxH:k},D(e))}))})}));return j.length?(0,b.jsxs)(s.kC,{align:"start",direction:"column",w:"full",gap:4,children:[t?(0,b.jsx)(f.__,{htmlFor:"test",fontSize:"xs",my:0,mr:1,children:t}):null,r?(0,b.jsx)(x.Z,{label:r}):null,A,Z.length?(0,b.jsx)(m,{label:null!==o&&void 0!==o?o:"Add new",options:Z.map((function(e){return z(e)})),onOptionSelected:I}):null]}):(0,b.jsx)(m,{label:null!==o&&void 0!==o?o:"Add new",options:Z.map((function(e){return z(e)})),onOptionSelected:I})}},86054:function(e,t,r){"use strict";var n=r(90849),i=r(90089),o=r(34896),s=r(38687),c=r(24246),u=["title","tooltip","children"];function l(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function a(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?l(Object(r),!0).forEach((function(t){(0,n.Z)(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):l(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}t.Z=function(e){var t=e.title,r=e.tooltip,n=e.children,l=(0,i.Z)(e,u);return(0,c.jsxs)(o.xu,a(a({borderRadius:"md",border:"1px solid",borderColor:"gray.200"},l),{},{children:[(0,c.jsxs)(o.X6,{as:"h3",fontSize:"sm",fontWeight:"semibold",color:"gray.700",py:4,px:6,backgroundColor:"gray.50",borderRadius:"md",textAlign:"left",children:[t,r?(0,c.jsx)(o.xv,{as:"span",mx:1,children:(0,c.jsx)(s.Z,{label:r})}):void 0]}),(0,c.jsx)(o.Kq,{p:6,spacing:6,children:n})]}))}},24753:function(e,t,r){"use strict";r.d(t,{MA:function(){return a},Vo:function(){return p},t5:function(){return d}});var n=r(90849),i=r(34896),o=r(24246);function s(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function c(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?s(Object(r),!0).forEach((function(t){(0,n.Z)(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):s(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}var u=function(e){var t=e.children;return(0,o.jsxs)(i.xv,{"data-testid":"toast-success-msg",children:[(0,o.jsx)("strong",{children:"Success:"})," ",t]})},l=function(e){var t=e.children;return(0,o.jsxs)(i.xv,{"data-testid":"toast-error-msg",children:[(0,o.jsx)("strong",{children:"Error:"})," ",t]})},a={variant:"subtle",position:"top",description:"",duration:5e3,status:"success",isClosable:!0},d=function(e){var t=(0,o.jsx)(u,{children:e});return c(c({},a),{description:t})},p=function(e){var t=(0,o.jsx)(l,{children:e});return c(c({},a),{description:t,status:"error"})}},21980:function(e,t,r){"use strict";var n=r(34896),i=r(29549),o=r(34090),s=r(86677),c=r(27378),u=r(6848),l=r(86054),a=r(43139),d=r(78624),p=r(60709),f=r(85375),x=r(49841),b=r(9865),j=r(24246),v=function(){var e,t=(0,u.C)(x.Zp),r=(0,u.C)(x.G1);(0,x.cq)({page:t,size:r});var n=(0,u.C)(x.w4),i=(0,o.u6)(),s=i.values,c=i.setFieldValue;return(0,j.jsx)(l.Z,{title:"Experiences",children:(0,j.jsx)(f.Z,{addButtonLabel:"Add experience",idField:"id",nameField:"name",allItems:n.map((function(e){return{id:e.id,name:e.name}})),values:null!==(e=s.experiences)&&void 0!==e?e:[],setValues:function(e){return c("experiences",e)},draggable:!0})})};t.Z=function(e){var t=e.property,r=e.handleSubmit,u=(0,s.useRouter)(),f=function(){u.push(p.ru)},x=(0,c.useMemo)((function(){return t||{name:"",type:b.uS.WEBSITE,experiences:[]}}),[t]);return(0,j.jsx)(o.J9,{enableReinitialize:!0,initialValues:x,onSubmit:r,children:function(e){var r=e.dirty,s=e.isValid,c=e.isSubmitting;return(0,j.jsxs)(o.l0,{style:{paddingTop:"12px",paddingBottom:"12px"},children:[(0,j.jsx)(n.xu,{py:3,children:(0,j.jsxs)(l.Z,{title:"Property details",children:[(0,j.jsx)(a.j0,{isRequired:!0,label:"Property name",name:"name",tooltip:"Unique name to identify this property",variant:"stacked"}),(0,j.jsx)(a.AP,{isRequired:!0,label:"Type",name:"type",options:(0,d.MM)(b.uS),variant:"stacked"})]})}),(0,j.jsx)(n.xu,{py:3,children:(0,j.jsx)(v,{})}),t&&(0,j.jsx)(n.xu,{py:3,children:(0,j.jsx)(l.Z,{title:"Advanced settings",children:(0,j.jsx)(a.Io,{label:"Property ID",name:"id",tooltip:"Automatically generated unique ID for this property, used for developer configurations",variant:"stacked",readOnly:!0})})}),(0,j.jsxs)(n.kC,{justifyContent:"right",width:"100%",paddingTop:2,children:[(0,j.jsx)(i.zx,{size:"sm",type:"submit",variant:"outline",isLoading:!1,mr:3,onClick:f,children:"Cancel"}),(0,j.jsx)(i.zx,{size:"sm",type:"submit",colorScheme:"primary",isDisabled:c||!r||!s,isLoading:c,children:"Save"})]})]})}})}},8303:function(e,t,r){"use strict";r.r(t);var n=r(55732),i=r(97865),o=r(34707),s=r.n(o),c=r(34896),u=r(70409),l=r(86677),a=r(78624),d=r(51471),p=r(60709),f=r(24753),x=r(31589),b=r(21980),j=r(33167),v=r(24246),h=function(){return(0,v.jsx)(c.xu,{display:"flex",alignItems:"center","data-testid":"header",children:(0,v.jsx)(c.X6,{fontSize:"2xl",fontWeight:"semibold",children:"Add property"})})};t.default=function(){var e=(0,u.pm)(),t=(0,l.useRouter)(),r=(0,x.dX)(),o=(0,i.Z)(r,1)[0],m=function(){var r=(0,n.Z)(s().mark((function r(n){var i,c;return s().wrap((function(r){for(;;)switch(r.prev=r.next){case 0:return r.next=2,o(n);case 2:if(i=r.sent,!(0,j.isErrorResult)(i)){r.next=6;break}return e((0,f.Vo)((0,a.e$)(i.error))),r.abrupt("return");case 6:c=i.data,e((0,f.t5)("Property ".concat(n.name," created successfully"))),t.push("".concat(p.ru,"/").concat(c.id));case 9:case"end":return r.stop()}}),r)})));return function(e){return r.apply(this,arguments)}}();return(0,v.jsxs)(d.Z,{title:"Add property",children:[(0,v.jsx)(h,{}),(0,v.jsxs)(c.xu,{maxWidth:"720px",pt:2,children:[(0,v.jsx)(c.xv,{fontSize:"sm",children:"Add new property to Fides here."}),(0,v.jsx)(b.Z,{handleSubmit:m})]})]})}},33167:function(e,t,r){"use strict";r.d(t,{isAPIError:function(){return n.Bw},isErrorResult:function(){return n.D4}});var n=r(60041)},25310:function(e,t,r){(window.__NEXT_P=window.__NEXT_P||[]).push(["/consent/properties/add-property",function(){return r(8303)}])},30808:function(e,t,r){"use strict";function n(e,t){if(null==e)return{};var r,n,i={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(i[r]=e[r]);return i}r.d(t,{Z:function(){return n}})},6983:function(e,t,r){"use strict";function n(e,t){return n=Object.setPrototypeOf?Object.setPrototypeOf.bind():function(e,t){return e.__proto__=t,e},n(e,t)}r.d(t,{Z:function(){return n}})}},function(e){e.O(0,[7751,6842,3452,3453,152,338,3702,9774,2888,179],(function(){return t=25310,e(e.s=t);var t}));var t=e.O();_N_E=t}]);