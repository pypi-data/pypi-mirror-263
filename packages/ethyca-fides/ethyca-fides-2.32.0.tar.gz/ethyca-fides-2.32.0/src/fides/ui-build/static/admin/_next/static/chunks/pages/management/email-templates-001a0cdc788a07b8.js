(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[1014],{86054:function(e,t,r){"use strict";var n=r(90849),i=r(90089),s=r(34896),o=r(38687),c=r(24246),a=["title","tooltip","children"];function u(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function l(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?u(Object(r),!0).forEach((function(t){(0,n.Z)(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):u(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}t.Z=function(e){var t=e.title,r=e.tooltip,n=e.children,u=(0,i.Z)(e,a);return(0,c.jsxs)(s.xu,l(l({borderRadius:"md",border:"1px solid",borderColor:"gray.200"},u),{},{children:[(0,c.jsxs)(s.X6,{as:"h3",fontSize:"sm",fontWeight:"semibold",color:"gray.700",py:4,px:6,backgroundColor:"gray.50",borderRadius:"md",textAlign:"left",children:[t,r?(0,c.jsx)(s.xv,{as:"span",mx:1,children:(0,c.jsx)(o.Z,{label:r})}):void 0]}),(0,c.jsx)(s.Kq,{p:6,spacing:6,children:n})]}))}},24753:function(e,t,r){"use strict";r.d(t,{MA:function(){return l},Vo:function(){return d},t5:function(){return p}});var n=r(90849),i=r(34896),s=r(24246);function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function c(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){(0,n.Z)(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}var a=function(e){var t=e.children;return(0,s.jsxs)(i.xv,{"data-testid":"toast-success-msg",children:[(0,s.jsx)("strong",{children:"Success:"})," ",t]})},u=function(e){var t=e.children;return(0,s.jsxs)(i.xv,{"data-testid":"toast-error-msg",children:[(0,s.jsx)("strong",{children:"Error:"})," ",t]})},l={variant:"subtle",position:"top",description:"",duration:5e3,status:"success",isClosable:!0},p=function(e){var t=(0,s.jsx)(a,{children:e});return c(c({},l),{description:t})},d=function(e){var t=(0,s.jsx)(u,{children:e});return c(c({},l),{description:t,status:"error"})}},28506:function(e,t,r){"use strict";r.r(t),r.d(t,{default:function(){return T}});var n=r(83125),i=r(34896),s=r(51471),o=r(90849),c=r(55732),a=r(97865),u=r(34707),l=r.n(u),p=r(70409),d=r(29549),f=r(34090),b=r(86054),m=r(43139),j=r(78624),g=r(24753),h=r(28703).u.injectEndpoints({endpoints:function(e){return{getMessagingTemplates:e.query({query:function(){return{url:"messaging/templates/"}},providesTags:function(){return["Messaging Templates"]}}),updateMessagingTemplates:e.mutation({query:function(e){return{url:"messaging/templates/",method:"PUT",body:e}},invalidatesTags:function(){return["Messaging Templates"]}})}}}),y=h.useGetMessagingTemplatesQuery,O=h.useUpdateMessagingTemplatesMutation,x=r(24246);function v(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function w(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?v(Object(r),!0).forEach((function(t){(0,o.Z)(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):v(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}var P=function(e){var t=e.emailTemplates,r=O(),n=(0,a.Z)(r,2),s=n[0],u=n[1].isLoading,h=(0,p.pm)(),y=function(){var e=(0,c.Z)(l().mark((function e(t,r){var n,i,o;return l().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n=function(e){if((0,j.D4)(e)){var n=(0,j.e$)(e.error,"An unexpected error occurred while editing the email templates. Please try again.");h((0,g.Vo)(n))}else h((0,g.t5)("Email templates saved.")),r.resetForm({values:t})},i=Object.entries(t).map((function(e){var t=(0,a.Z)(e,2);return{key:t[0],content:t[1].content}})),e.next=4,s(i);case 4:o=e.sent,n(o);case 6:case"end":return e.stop()}}),e)})));return function(t,r){return e.apply(this,arguments)}}(),v=t.reduce((function(e,t){return w(w({},e),{},(0,o.Z)({},t.key,{label:t.label,content:t.content}))}),{});return(0,x.jsx)(f.J9,{enableReinitialize:!0,initialValues:v,onSubmit:y,children:function(){return(0,x.jsxs)(f.l0,{style:{paddingTop:"12px",paddingBottom:"12px"},children:[Object.entries(v).map((function(e){var t=(0,a.Z)(e,2),r=t[0],n=t[1];return(0,x.jsx)(i.xu,{py:3,children:(0,x.jsxs)(b.Z,{title:n.label,children:[(0,x.jsx)(m.j0,{label:"Message subject",name:"".concat(r,".content.subject"),variant:"stacked"}),(0,x.jsx)(m.Ks,{label:"Message body",name:"".concat(r,".content.body"),variant:"stacked",resize:!0})]})},r)})),(0,x.jsx)(i.kC,{justifyContent:"right",width:"100%",paddingTop:2,children:(0,x.jsx)(d.zx,{size:"sm",type:"submit",colorScheme:"primary",isLoading:u,children:"Save"})})]})}})},T=function(){var e=y(),t=e.data;return e.isLoading?(0,x.jsx)(s.Z,{title:"Email templates",children:(0,x.jsx)(n.$,{})}):(0,x.jsx)(s.Z,{title:"Email templates",children:(0,x.jsxs)(i.xu,{"data-testid":"email-templates",children:[(0,x.jsx)(i.X6,{marginBottom:2,fontSize:"2xl",children:"Email templates"}),(0,x.jsxs)(i.xu,{maxWidth:"720px",children:[(0,x.jsx)(i.xv,{fontSize:"sm",children:"When privacy requests are submitted, Fides emails the data subject to confirm their identity and keep them updated on the status of the request. The templates below allow you to configure the subject and body of the email to suit your business needs. To change the appearance of the email, you may use the editors within your messaging provider (e.g. Mailgun, SendGrid, Twilio)."}),(0,x.jsx)(i.xu,{padding:2,children:(0,x.jsx)(P,{emailTemplates:t})})]})]})})}},8334:function(e,t,r){(window.__NEXT_P=window.__NEXT_P||[]).push(["/management/email-templates",function(){return r(28506)}])},30808:function(e,t,r){"use strict";function n(e,t){if(null==e)return{};var r,n,i={},s=Object.keys(e);for(n=0;n<s.length;n++)r=s[n],t.indexOf(r)>=0||(i[r]=e[r]);return i}r.d(t,{Z:function(){return n}})},6983:function(e,t,r){"use strict";function n(e,t){return n=Object.setPrototypeOf?Object.setPrototypeOf.bind():function(e,t){return e.__proto__=t,e},n(e,t)}r.d(t,{Z:function(){return n}})}},function(e){e.O(0,[7751,6842,3453,338,3702,9774,2888,179],(function(){return t=8334,e(e.s=t);var t}));var t=e.O();_N_E=t}]);