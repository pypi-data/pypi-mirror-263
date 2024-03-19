(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[354],{57595:function(e,t,n){"use strict";var r=n(90849),i=n(34896),s=n(24246);function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}t.Z=function(e){return(0,s.jsx)(i.rU,function(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){(0,r.Z)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}({isExternal:!0,color:"complimentary.500"},e))}},33976:function(e,t,n){"use strict";n.r(t),n.d(t,{default:function(){return Y}});var r=n(34896),i=n(27378),s=n(51471),a=n(90849),o=n(29549),c=n(92222),l=n(59003),u=n(55162),d=n(79894),p=n.n(d),h=n(86677),x=n(60709),f=n(63238),y=n(21084),g=n(55732),b=n(97865),j=n(34707),v=n.n(j),m=n(70409),w=n(60530),O=n(44833),P=n(57595),C=n(78624),S=n(24753),_=n(44047),E=n(24246);function z(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function D(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?z(Object(n),!0).forEach((function(t){(0,a.Z)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):z(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}var R=function(e){var t=e.isOpen,n=e.onClose,s=e.testId,a=void 0===s?"custom-asset-modal":s,c=e.assetType,l=(0,i.useRef)(null),u=(0,i.useState)(null),d=u[0],p=u[1],h=(0,m.pm)(),x=(0,O.uI)({onDrop:function(e){var t;"css"===(null===(t=e[0].name.split(".").pop())||void 0===t?void 0:t.toLowerCase())?p(e[0]):h((0,S.Vo)("Only css files are allowed."))}}),f=x.getRootProps,y=x.getInputProps,j=x.isDragActive,z=(0,_.JQ)(),R=(0,b.Z)(z,2),k=R[0],T=R[1].isLoading,I=function(){var e=(0,g.Z)(v().mark((function e(){var t;return v().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!d){e.next=9;break}return e.next=3,k({assetType:c,file:d});case 3:if(t=e.sent,!(0,C.D4)(t)){e.next=7;break}return h((0,S.Vo)((0,C.e$)(t.error))),e.abrupt("return");case 7:h((0,S.t5)("Stylesheet uploaded successfully")),n();case 9:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}();return(0,E.jsxs)(w.u_,{initialFocusRef:l,isOpen:t,onClose:n,size:"2xl",children:[(0,E.jsx)(w.ZA,{}),(0,E.jsxs)(w.hz,{textAlign:"left",p:2,"data-testid":a,children:[(0,E.jsx)(w.xB,{tabIndex:-1,ref:l,children:"Upload stylesheet"}),(0,E.jsxs)(w.fe,{children:[(0,E.jsxs)(r.xv,{fontSize:"sm",mb:4,children:["To customize the appearance of your consent experiences, you may upload a CSS stylesheet. To download a template as a helpful starting point, click"," ",(0,E.jsx)(P.Z,{href:"https://raw.githubusercontent.com/ethyca/fides/main/clients/fides-js/src/components/fides.css",isExternal:!0,children:"here"}),"."," ",(0,E.jsx)(P.Z,{href:"https://fid.es/customize-styles",isExternal:!0,children:"Learn more"}),"."]}),(0,E.jsxs)(r.xu,D(D({},f()),{},{bg:j?"gray.100":"gray.50",border:"2px dashed",borderColor:j?"gray.300":"gray.200",borderRadius:"md",cursor:"pointer",minHeight:"150px",display:"flex",alignItems:"center",justifyContent:"center",textAlign:"center",children:[(0,E.jsx)("input",D({},y())),d?(0,E.jsx)(r.xv,{children:d.name}):j?(0,E.jsx)(r.xv,{children:"Drop the file here..."}):(0,E.jsx)(r.xv,{children:"Click or drag and drop your file here."})]}))]}),(0,E.jsx)(w.mz,{children:(0,E.jsxs)(o.hE,{size:"sm",spacing:"2",width:"100%",display:"flex",justifyContent:"right",children:[(0,E.jsx)(o.zx,{variant:"outline",onClick:n,"data-testid":"cancel-btn",isDisabled:T,children:"Cancel"}),(0,E.jsx)(o.zx,{colorScheme:"primary",type:"submit",isDisabled:!d||T,onClick:I,"data-testid":"submit-btn",children:"Submit"})]})})]})]})},k=function(e){var t=e.assetType,n=(0,y.qY)();return(0,E.jsxs)(E.Fragment,{children:[(0,E.jsx)(o.zx,{variant:"outline",size:"xs",ml:2,onClick:n.onOpen,children:"Upload stylesheet"}),(0,E.jsx)(R,{isOpen:n.isOpen,onClose:n.onClose,assetType:t})]})},T=n(57984),I=new Map([["overlay","Overlay"],["privacy_center","Privacy center"],["tcf_overlay","TCF overlay"],["modal","Modal"],["banner_and_modal","Banner and modal"]]),Z=(new Map([["always_enabled","Always enabled"],["always_disabled","Always disabled"],["enabled_where_required","Enabled where legally required"]]),n(49841)),M=n(56602),F=n(90768),A=n(91728),N="{privacy-center-hostname-and-path}",V='<script src="https://'.concat(N,'/fides.js"><\/script>'),L="<script>Fides.gtm()<\/script>",U=function(){var e=(0,y.qY)(),t=(0,i.useRef)(null),n=(0,F.hz)().fidesCloud,s=(0,_.Vh)(void 0,{skip:!n}),a=s.data,c=s.isSuccess,l=(0,i.useMemo)((function(){return n&&c&&null!==a&&void 0!==a&&a.privacy_center_url?V.replace(N,a.privacy_center_url):V}),[null===a||void 0===a?void 0:a.privacy_center_url,n,c]);return(0,E.jsxs)(E.Fragment,{children:[(0,E.jsx)(o.zx,{onClick:e.onOpen,variant:"outline",size:"xs",rightIcon:(0,E.jsx)(A.TI,{}),"data-testid":"js-tag-btn",children:"Get JavaScript tag"}),(0,E.jsxs)(w.u_,{isOpen:e.isOpen,onClose:e.onClose,isCentered:!0,size:"xl",initialFocusRef:t,children:[(0,E.jsx)(w.ZA,{}),(0,E.jsxs)(w.hz,{"data-testid":"copy-js-tag-modal",children:[(0,E.jsx)(w.xB,{tabIndex:-1,ref:t,pb:0,children:"Copy JavaScript tag"}),(0,E.jsx)(w.fe,{pt:3,pb:6,children:(0,E.jsxs)(r.Kq,{spacing:3,children:[(0,E.jsx)(r.xv,{children:"Copy the code below and paste it onto every page of your website, as high up in the <head> as possible. Replace the bracketed component with your privacy center's hostname and path."}),(0,E.jsxs)(r.EK,{display:"flex",justifyContent:"space-between",alignItems:"center",p:0,children:[(0,E.jsx)(r.xv,{p:4,children:l}),(0,E.jsx)(M.Z,{copyText:l})]}),(0,E.jsx)(r.xv,{children:"Optionally, you can enable Google Tag Manager for managing tags on your website by including the script tag below along with the Fides.js tag. Place it below the Fides.js script tag."}),(0,E.jsxs)(r.EK,{display:"flex",justifyContent:"space-between",alignItems:"center",p:0,children:[(0,E.jsx)(r.xv,{p:4,children:L}),(0,E.jsx)(M.Z,{copyText:L})]}),(0,E.jsxs)(r.xv,{children:["For more information about adding a JavaScript tag to your website, please visit"," ",(0,E.jsx)(r.rU,{color:"complimentary.500",href:"https://docs.ethyca.com/tutorials/consent-management-configuration/install-fides#install-fidesjs-script-on-your-website",isExternal:!0,children:"docs.ethyca.com"})]})]})})]})]})]})},W=n(91381),q=n(9865);function G(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function B(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?G(Object(n),!0).forEach((function(t){(0,a.Z)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):G(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}var J={items:[],total:0,page:1,size:25,pages:1},H=function(){return(0,E.jsxs)(r.gC,{mt:6,p:10,spacing:4,borderRadius:"base",maxW:"70%","data-testid":"empty-state",alignSelf:"center",margin:"auto",children:[(0,E.jsxs)(r.gC,{children:[(0,E.jsx)(r.xv,{fontSize:"md",fontWeight:"600",children:"No privacy experiences found."}),(0,E.jsx)(r.xv,{fontSize:"sm",children:'Click "Create new experience" to add your first privacy experience to Fides.'})]}),(0,E.jsx)(p(),{href:"".concat(x.w0,"/new"),children:(0,E.jsx)(o.zx,{size:"xs",colorScheme:"primary","data-testid":"add-privacy-experience-btn",children:"Create new experience"})})]})},K=(0,c.Cl)(),X=function(){var e=(0,_.x8)().isLoading,t=(0,h.useRouter)(),n=(0,f.Tg)([q.Sh.PRIVACY_EXPERIENCE_UPDATE]),s=(0,u.oi)(),a=s.PAGE_SIZES,d=s.pageSize,y=s.setPageSize,j=s.onPreviousPageClick,m=s.isPreviousPageDisabled,w=s.onNextPageClick,O=s.isNextPageDisabled,P=s.startRange,C=s.endRange,S=s.pageIndex,z=s.setTotalPages,D=(0,Z.cq)({page:S,size:d}),R=D.isFetching,M=D.isLoading,F=D.data,A=(0,i.useMemo)((function(){return F||J}),[F]),N=A.items,V=A.total,L=A.pages;(0,i.useEffect)((function(){z(L)}),[L,z]);var G=(0,i.useMemo)((function(){return[K.accessor((function(e){return e.name}),{id:"name",cell:function(e){return(0,E.jsx)(u.G3,{value:e.getValue()})},header:function(e){return(0,E.jsx)(u.Rr,B({value:"Title"},e))}}),K.accessor((function(e){return e.component}),{id:"component",cell:function(e){return function(e){var t,n=null!==(t=I.get(e))&&void 0!==t?t:e;return(0,E.jsx)(T.G3,{value:n})}(e.getValue())},header:function(e){return(0,E.jsx)(u.Rr,B({value:"Component"},e))}}),K.accessor((function(e){return e.regions}),{id:"regions",cell:function(e){return(0,E.jsx)(u.WP,B({suffix:"Locations",value:(0,W.JL)(e.getValue())},e))},header:function(e){return(0,E.jsx)(u.Rr,B({value:"Locations"},e))},meta:{displayText:"Locations",showHeaderMenu:!0}}),K.accessor((function(e){return e.properties.map((function(e){return e.name}))}),{id:"properties",cell:function(e){return(0,E.jsx)(u.WP,B({suffix:"Properties",value:e.getValue()},e))},header:function(e){return(0,E.jsx)(u.Rr,B({value:"Properties"},e))},meta:{displayText:"Properties",showHeaderMenu:!0}}),K.accessor((function(e){return e.updated_at}),{id:"updated_at",cell:function(e){return(0,E.jsx)(u.G3,{value:new Date(e.getValue()).toDateString()})},header:function(e){return(0,E.jsx)(u.Rr,B({value:"Last update"},e))}}),n&&K.accessor((function(e){return e.disabled}),{id:"enable",cell:function(e){return function(e){var t=e.row,n=e.getValue,r=(0,Z.o3)(),i=(0,b.Z)(r,1)[0],s=function(){var e=(0,g.Z)(v().mark((function e(n){return v().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.abrupt("return",i({id:t.original.id,disabled:!n}));case 1:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),a=n(),o=t.original.regions,c=!!o&&o.length>1,l=c?"Disabling multiple states":"Disabling experience",u=c?"Warning, you are about to disable this privacy experience for multiple locations. If you continue, your privacy notices will not be accessible to users in these locations.":"Warning, you are about to disable this privacy experience. If you continue, your privacy notices will not be accessible to users in this location.";return(0,E.jsx)(T.S1,{value:a,onToggle:s,title:l,message:u})}(e)},header:function(e){return(0,E.jsx)(u.Rr,B({value:"Enable"},e))}})].filter(Boolean)}),[n]),X=(0,l.b7)({getCoreRowModel:(0,c.sC)(),getGroupedRowModel:(0,c.qe)(),getExpandedRowModel:(0,c.rV)(),columns:G,manualPagination:!0,data:N,state:{expanded:!0}});return M||e?(0,E.jsx)(u.I4,{rowHeight:36,numRows:15}):(0,E.jsx)("div",{children:(0,E.jsxs)(r.kC,{flex:1,direction:"column",overflow:"auto",children:[n&&(0,E.jsxs)(u.Q$,{children:[(0,E.jsxs)(r.Ug,{alignItems:"center",spacing:4,children:[(0,E.jsx)(U,{}),(0,E.jsx)(f.ZP,{scopes:[q.Sh.CUSTOM_ASSET_UPDATE],children:(0,E.jsx)(k,{assetType:q.Db.CUSTOM_FIDES_CSS})})]}),(0,E.jsx)(p(),{href:"".concat(x.w0,"/new"),children:(0,E.jsx)(o.zx,{size:"xs",colorScheme:"primary","data-testid":"add-privacy-ecperience-btn",children:"Create new experience"})})]}),(0,E.jsx)(u.ZK,{tableInstance:X,onRowClick:n?function(e){var r=e.id;n&&t.push("".concat(x.w0,"/").concat(r))}:void 0,emptyTableNotice:(0,E.jsx)(H,{})}),(0,E.jsx)(u.s8,{totalRows:V,pageSizes:a,setPageSize:y,onPreviousPageClick:j,isPreviousPageDisabled:m||R,onNextPageClick:w,isNextPageDisabled:O||R,startRange:P,endRange:C})]})})},Y=function(){return(0,E.jsxs)(s.Z,{title:"Privacy experiences",children:[(0,E.jsx)(r.xu,{mb:4,children:(0,E.jsx)(r.X6,{fontSize:"2xl",fontWeight:"semibold",mb:2,"data-testid":"header",children:"Privacy experience"})}),(0,E.jsx)(r.xv,{fontSize:"sm",mb:8,width:{base:"100%",lg:"70%"},children:"Based on your privacy notices, Fides has created the overlay and privacy experience configuration below. Your privacy notices will be presented by region in these components. Edit each component to adjust the text that displays in the privacy center, overlay, and banners that show your notices. When you\u2019re ready to include these privacy notices on your website, copy the javascript using the button on this page and place it on your website."}),(0,E.jsx)(r.xu,{"data-testid":"privacy-experience-page",children:(0,E.jsx)(X,{})})]})}},55173:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/consent/privacy-experience",function(){return n(33976)}])}},function(e){e.O(0,[7751,530,3452,7140,5181,378,4833,338,5162,4429,958,9774,2888,179],(function(){return t=55173,e(e.s=t);var t}));var t=e.O();_N_E=t}]);