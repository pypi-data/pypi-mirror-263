(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[3709],{62905:function(e,n,t){"use strict";t.d(n,{Dd:function(){return j},Oy:function(){return g},XK:function(){return f},bH:function(){return x}});var s=t(90849),r=t(77751),i=t(34896),o=t(62332),a=t(29549),u=t(60530),c=t(27378),l=t(24246);function d(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);n&&(s=s.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,s)}return t}function p(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?d(Object(t),!0).forEach((function(n){(0,s.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):d(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var f=function(e,n){var t=e.filter((function(e){return e.isChecked}));return t.length>0?"".concat(n,"=").concat(t.map((function(e){return e.value})).join("&".concat(n,"="))):void 0},h=function(e){var n=e.value,t=e.displayText,s=e.isChecked,o=e.onCheckboxChange;return(0,l.jsx)(r.XZ,{value:n,height:"20px",mb:"25px",isChecked:s,onChange:function(e){var t=e.target;o(n,t.checked)},_focusWithin:{bg:"gray.100"},colorScheme:"complimentary",children:(0,l.jsx)(i.xv,{fontSize:"sm",lineHeight:5,textOverflow:"ellipsis",overflow:"hidden",children:t})},n)},x=function(e){var n=e.options,t=e.header,s=e.onCheckboxChange,r=e.columns,u=void 0===r?3:r,d=e.numDefaultOptions,f=void 0===d?15:d,x=(0,c.useState)(!1),g=x[0],j=x[1],b=g?n:n.slice(0,f),C=n.length>f;return(0,l.jsxs)(o.Qd,{border:"0px",padding:"12px 8px 8px 12px",children:[(0,l.jsx)(i.X6,{height:"56px",children:(0,l.jsxs)(o.KF,{height:"100%",children:[(0,l.jsx)(i.xu,{flex:"1",alignItems:"center",justifyContent:"center",textAlign:"left",fontWeight:600,children:t}),(0,l.jsx)(o.XE,{})]})}),(0,l.jsxs)(o.Hk,{id:"panel-".concat(t),children:[(0,l.jsx)(i.MI,{columns:u,children:b.map((function(e){return(0,l.jsx)(h,p(p({},e),{},{onCheckboxChange:s}),e.value)}))}),!g&&C?(0,l.jsx)(a.zx,{size:"sm",variant:"ghost",onClick:function(){j(!0)},children:"View more"}):null,g&&C?(0,l.jsx)(a.zx,{size:"sm",variant:"ghost",onClick:function(){j(!1)},children:"View less"}):null]})]})},g=function(e){var n=e.heading,t=e.children;return(0,l.jsxs)(i.xu,{padding:"12px 8px 8px 12px",maxHeight:600,children:[n?(0,l.jsx)(i.X6,{size:"md",lineHeight:6,fontWeight:"bold",mb:2,children:n}):null,t]})},j=function(e){var n=e.isOpen,t=e.onClose,s=e.children,r=e.resetFilters;return(0,l.jsxs)(u.u_,{isOpen:n,onClose:t,isCentered:!0,size:"2xl",children:[(0,l.jsx)(u.ZA,{}),(0,l.jsxs)(u.hz,{children:[(0,l.jsx)(u.xB,{children:"Filters"}),(0,l.jsx)(u.ol,{}),(0,l.jsx)(i.iz,{}),(0,l.jsx)(u.fe,{maxH:"85vh",padding:"0px",overflowX:"auto",style:{scrollbarGutter:"stable"},children:s}),(0,l.jsx)(u.mz,{children:(0,l.jsxs)(i.xu,{display:"flex",justifyContent:"space-between",width:"100%",children:[(0,l.jsx)(a.zx,{variant:"outline",size:"sm",mr:3,onClick:r,flexGrow:1,children:"Reset filters"}),(0,l.jsx)(a.zx,{colorScheme:"primary",size:"sm",onClick:t,flexGrow:1,children:"Done"})]})})]})]})}},65535:function(e,n,t){"use strict";t.d(n,{ZS:function(){return a},a4:function(){return i}});var s=t(80406),r=t(28703).u.injectEndpoints({endpoints:function(e){return{getPurposes:e.query({query:function(){return"purposes"}})}}}),i=r.useGetPurposesQuery,o={purposes:{},special_purposes:{}},a=(0,s.P1)(r.endpoints.getPurposes.select(),(function(e){return e.data||o}))},11488:function(e,n,t){"use strict";t.r(n),t.d(n,{default:function(){return X}});var s=t(34896),r=t(27378),i=t(51471),o=t(90849),a=t(29549),u=t(92222),c=t(59003),l=t(90768),d=t(55162),p=t(86677),f=t(62905),h=t(60709),x=t(23571),g=t(73679),j=t(21084),b=t(62332),C=t(6848),v=t(65535),O=t(75846),m=t(24246);function y(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);n&&(s=s.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,s)}return t}function k(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?y(Object(t),!0).forEach((function(n){(0,o.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):y(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var P=function(e){var n=e.isOpen,t=e.isTcfEnabled,s=e.onClose,r=e.resetFilters,i=e.purposeOptions,o=e.onPurposeChange,a=e.dataUseOptions,u=e.onDataUseChange,c=e.legalBasisOptions,l=e.onLegalBasisChange,d=e.consentCategoryOptions,p=e.onConsentCategoryChange;return(0,m.jsx)(f.Dd,{isOpen:n,onClose:s,resetFilters:r,children:(0,m.jsx)(b.UQ,{children:(0,m.jsxs)(f.Oy,{children:[t?(0,m.jsx)(f.bH,{options:i,onCheckboxChange:o,header:"TCF purposes",columns:1,numDefaultOptions:5}):null,(0,m.jsx)(f.bH,{options:a,onCheckboxChange:u,header:"Data uses"}),t?(0,m.jsx)(f.bH,{options:c,onCheckboxChange:l,header:"Legal basis"}):null,t?null:(0,m.jsx)(f.bH,{options:d,onCheckboxChange:p,header:"Consent categories"})]})})})},w=t(97865),_=t(60530),D=t(83125),z=t(34090),S=t(43139),E=t(44047),T=function(e){var n=e.isOpen,t=e.onClose,r=e.fidesKey,i=(0,E.ho)(r),o=i.data,u=i.isLoading;return(0,m.jsxs)(_.u_,{isOpen:n,onClose:t,size:"xxl",returnFocusOnClose:!1,isCentered:!0,children:[(0,m.jsx)(_.ZA,{}),(0,m.jsxs)(_.hz,{maxWidth:"800px",children:[(0,m.jsx)(_.xB,{children:"Vendor"}),(0,m.jsx)(_.fe,{children:u?(0,m.jsx)(s.kC,{width:"100%",height:"324px",alignItems:"center",justifyContent:"center",children:(0,m.jsx)(D.$,{})}):(0,m.jsx)(z.J9,{initialValues:o,enableReinitialize:!0,onSubmit:function(){},children:function(e){var n=e.values;return(0,m.jsxs)(z.l0,{children:[(0,m.jsx)(s.xu,{mb:6,children:(0,m.jsx)(S.j0,{label:"Vendor Name",variant:"stacked",name:"name",disabled:!0})}),Object.entries((null===n||void 0===n?void 0:n.purposes)||{}).length>0?(0,m.jsx)(S.__,{children:" Purposes "}):null,(0,m.jsx)(z.F2,{name:"purposes",render:function(){return(0,m.jsx)(b.UQ,{allowMultiple:!0,children:Object.entries(n.purposes).map((function(e,n){var t=(0,w.Z)(e,1)[0];return(0,m.jsx)(b.Qd,{children:function(e){var n=e.isExpanded;return(0,m.jsxs)(m.Fragment,{children:[(0,m.jsxs)(b.KF,{backgroundColor:n?"gray.50":"unset",children:[(0,m.jsx)(s.xu,{flex:"1",textAlign:"left",children:t}),(0,m.jsx)(b.XE,{})]}),(0,m.jsxs)(b.Hk,{backgroundColor:"gray.50",children:[(0,m.jsx)(s.xu,{my:4,children:(0,m.jsx)(S.VT,{label:"Data Uses",isMulti:!0,disableMenu:!0,isDisabled:!0,options:[],variant:"stacked",name:"purposes['".concat(t,"'].data_uses")})}),(0,m.jsx)(S.VT,{label:"Legal Basis",isMulti:!0,disableMenu:!0,isDisabled:!0,options:[],variant:"stacked",name:"purposes['".concat(t,"'].legal_bases")})]})]})}},n)}))})}}),(0,m.jsx)(s.xu,{my:4,children:(0,m.jsx)(S.VT,{label:"Features",isMulti:!0,options:[],disableMenu:!0,isDisabled:!0,variant:"stacked",name:"features"})}),(0,m.jsx)(S.VT,{label:"Data Categories",isMulti:!0,options:[],disableMenu:!0,isDisabled:!0,variant:"stacked",name:"data_categories"})]})}})}),(0,m.jsxs)(_.mz,{children:[(0,m.jsxs)(a.zx,{variant:"outline",size:"sm",onClick:t,children:["Close"," "]}),(0,m.jsx)(s.LZ,{})]})]})]})};function F(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);n&&(s=s.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,s)}return t}function M(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?F(Object(t),!0).forEach((function(n){(0,o.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):F(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var R=(0,u.Cl)(),V={items:[],total:0,page:1,size:25,pages:1},Z=function(){var e=(0,l.hz)(),n=e.tcf,t=e.dictionaryService,i=(0,E.x8)().isLoading,o=function(){var e=(0,j.qY)();return{isOpen:e.isOpen,onOpen:e.onOpen,onClose:e.onClose}}(),b=o.isOpen,y=o.onOpen,w=o.onClose,_=(0,p.useRouter)(),D=(0,r.useState)(),z=D[0],S=D[1],F=function(){var e=(0,j.qY)(),n=e.isOpen,t=e.onClose,s=e.onOpen;(0,O.fd)();var i=(0,C.C)(O.U3);(0,v.a4)();var o=(0,C.C)(v.ZS),a=(0,r.useState)([]),u=a[0],c=a[1],l=(0,r.useState)([]),d=l[0],p=l[1],f=(0,r.useState)([{displayText:"Consent",value:"Consent",isChecked:!1},{displayText:"Legitimate Interest",value:"Legitimate interests",isChecked:!1}]),h=f[0],x=f[1],b=(0,r.useState)([{displayText:"Advertising",value:"advertising",isChecked:!1},{displayText:"Analytics",value:"analytics",isChecked:!1},{displayText:"Functional",value:"functional",isChecked:!1},{displayText:"Essential",value:"essential",isChecked:!1}]),m=b[0],y=b[1];(0,r.useEffect)((function(){0===d.length&&p(i.map((function(e){return{value:e.fides_key,displayText:e.name||e.fides_key,isChecked:!1}})))}),[i,d,p]),(0,r.useEffect)((function(){0===u.length&&c([].concat((0,g.Z)(Object.entries(o.purposes).map((function(e){return{value:"normal.".concat(e[0]),displayText:e[1].name,isChecked:!1}}))),(0,g.Z)(Object.entries(o.special_purposes).map((function(e){return{value:"special.".concat(e[0]),displayText:e[1].name,isChecked:!1}})))))}),[o,u,p]);var P=function(e,n,t,s){s(t.map((function(t){return t.value===e?k(k({},t),{},{isChecked:n}):t})))};return{isOpen:n,onClose:t,onOpen:s,resetFilters:function(){p((function(e){return e.map((function(e){return k(k({},e),{},{isChecked:!1})}))})),x((function(e){return e.map((function(e){return k(k({},e),{},{isChecked:!1})}))})),c((function(e){return e.map((function(e){return k(k({},e),{},{isChecked:!1})}))})),y((function(e){return e.map((function(e){return k(k({},e),{},{isChecked:!1})}))}))},purposeOptions:u,onPurposeChange:function(e,n){P(e,n,u,c)},dataUseOptions:d,onDataUseChange:function(e,n){P(e,n,d,p)},legalBasisOptions:h,onLegalBasisChange:function(e,n){P(e,n,h,x)},consentCategoryOptions:m,onConsentCategoryChange:function(e,n){P(e,n,m,y)}}}(),Z=F.isOpen,U=F.onOpen,X=F.onClose,L=F.resetFilters,A=F.purposeOptions,B=F.onPurposeChange,H=F.dataUseOptions,I=F.onDataUseChange,K=F.legalBasisOptions,N=F.onLegalBasisChange,G=F.consentCategoryOptions,Q=F.onConsentCategoryChange,W=(0,r.useMemo)((function(){return(0,f.XK)(H,"data_uses")}),[H]),q=(0,r.useMemo)((function(){return(0,f.XK)(K,"legal_bases")}),[K]),Y=(0,r.useMemo)((function(){var e=A.filter((function(e){return e.value.includes("normal")})).map((function(e){return M(M({},e),{},{value:e.value.split(".")[1]})}));return(0,f.XK)(e,"purposes")}),[A]),$=(0,r.useMemo)((function(){var e=A.filter((function(e){return e.value.includes("special")})).map((function(e){return M(M({},e),{},{value:e.value.split(".")[1]})}));return(0,f.XK)(e,"special_purposes")}),[A]),J=(0,r.useMemo)((function(){return(0,f.XK)(G,"consent_category")}),[G]),ee=(0,d.oi)(),ne=ee.PAGE_SIZES,te=ee.pageSize,se=ee.setPageSize,re=ee.onPreviousPageClick,ie=ee.isPreviousPageDisabled,oe=ee.onNextPageClick,ae=ee.isNextPageDisabled,ue=ee.startRange,ce=ee.endRange,le=ee.pageIndex,de=ee.setTotalPages,pe=ee.resetPageIndexToDefault,fe=(0,r.useState)(),he=fe[0],xe=fe[1],ge=(0,E.de)({pageIndex:le,pageSize:te,dataUses:W,search:he,legalBasis:q,purposes:Y,specialPurposes:$,consentCategories:J}),je=ge.isFetching,be=ge.isLoading,Ce=ge.data,ve=(0,r.useMemo)((function(){return Ce||V}),[Ce]),Oe=ve.items,me=ve.total,ye=ve.pages;(0,r.useEffect)((function(){de(ye)}),[ye,de]);var ke=(0,r.useMemo)((function(){return[R.accessor((function(e){return e.name}),{id:"name",cell:function(e){return(0,m.jsx)(d.G3,{value:e.getValue()})},header:function(e){return(0,m.jsx)(d.Rr,M({value:"Vendor"},e))}}),R.accessor((function(e){return e.data_uses}),{id:"tcf_purpose",cell:function(e){return(0,m.jsx)(d.A4,{suffix:"purposes",value:e.getValue()})},header:function(e){return(0,m.jsx)(d.Rr,M({value:"TCF purpose"},e))}}),R.accessor((function(e){return e.data_uses}),{id:"data_uses",cell:function(e){return(0,m.jsx)(d.A4,{suffix:"data uses",value:e.getValue()})},header:function(e){return(0,m.jsx)(d.Rr,M({value:"Data use"},e))}}),R.accessor((function(e){return e.legal_bases}),{id:"legal_bases",cell:function(e){return(0,m.jsx)(d.A4,{suffix:"bases",value:e.getValue()})},header:function(e){return(0,m.jsx)(d.Rr,M({value:"Legal basis"},e))}}),R.accessor((function(e){return e.consent_categories}),{id:"consent_categories",cell:function(e){return(0,m.jsx)(d.A4,{suffix:"Categories",value:e.getValue()})},header:function(e){return(0,m.jsx)(d.Rr,M({value:"Categories"},e))}}),R.accessor((function(e){return e.cookies}),{id:"cookies",cell:function(e){return(0,m.jsx)(d.A4,{suffix:"Cookies",value:e.getValue()})},header:function(e){return(0,m.jsx)(d.Rr,M({value:"Cookies"},e))}})]}),[]),Pe=(0,c.b7)({columns:ke,data:Oe,state:{columnVisibility:{tcf_purpose:n,data_uses:n,legal_bases:n,consent_categories:!n,cookies:!n}},getCoreRowModel:(0,u.sC)(),columnResizeMode:"onChange",enableColumnResizing:!0});return be||i?(0,m.jsx)(d.I4,{rowHeight:36,numRows:15}):(0,m.jsxs)(s.kC,{flex:1,direction:"column",overflow:"auto",children:[b&&z?(0,m.jsx)(T,{isOpen:b,fidesKey:z,onClose:w}):null,(0,m.jsxs)(d.Q$,{children:[(0,m.jsx)(d.HO,{globalFilter:he,setGlobalFilter:function(e){pe(),xe(e)},placeholder:"Search"}),(0,m.jsx)(P,{isOpen:Z,isTcfEnabled:n,onClose:X,resetFilters:L,purposeOptions:A,onPurposeChange:B,dataUseOptions:H,onDataUseChange:I,legalBasisOptions:K,onLegalBasisChange:N,consentCategoryOptions:G,onConsentCategoryChange:Q}),(0,m.jsxs)(s.Ug,{alignItems:"center",spacing:4,children:[(0,m.jsx)(x.Z,{buttonLabel:"Add vendors",buttonVariant:"outline",onButtonClick:t?function(){_.push(h.Gg)}:void 0}),(0,m.jsx)(a.zx,{onClick:U,"data-testid":"filter-multiple-systems-btn",size:"xs",variant:"outline",children:"Filter"})]})]}),(0,m.jsx)(d.ZK,{tableInstance:Pe,onRowClick:function(e){S(e.fides_key),y()}}),(0,m.jsx)(d.s8,{totalRows:me,pageSizes:ne,setPageSize:se,onPreviousPageClick:re,isPreviousPageDisabled:ie||je,onNextPageClick:oe,isNextPageDisabled:ae||je,startRange:ue,endRange:ce})]})},U=function(e){var n=e.title,t=e.description;return(0,m.jsxs)(m.Fragment,{children:[(0,m.jsx)(s.xu,{mb:4,children:(0,m.jsx)(s.X6,{fontSize:"2xl",fontWeight:"semibold",mb:2,"data-testid":"header",children:n})}),(0,m.jsx)(s.kC,{children:(0,m.jsx)(s.xv,{fontSize:"sm",mb:8,width:{base:"100%",lg:"50%"},children:t})})]})},X=function(){return(0,m.jsxs)(i.Z,{title:"Configure consent",children:[(0,m.jsx)(U,{title:"Manage your vendors",description:"Use the table below to manage your vendors. Modify the legal basis for a vendor if permitted and view and group your views by applying different filters"}),(0,m.jsx)(Z,{})]})}},54727:function(e,n,t){(window.__NEXT_P=window.__NEXT_P||[]).push(["/consent/configure",function(){return t(11488)}])}},function(e){e.O(0,[7751,530,6842,3452,3453,8301,7140,5181,338,3702,5162,3571,9774,2888,179],(function(){return n=54727,e(e.s=n);var n}));var n=e.O();_N_E=n}]);