import{c as f,d as o}from"./VSelectionControl-DiMGQAeK.js";import{x as V,co as h,G as v,ar as c,h as l,K as x,ah as I,L as k,am as b}from"./admin-drawer-panel-B_bfGEw2.js";const C=V({indeterminate:Boolean,indeterminateIcon:{type:h,default:"$checkboxIndeterminate"},...f({falseIcon:"$checkboxOff",trueIcon:"$checkboxOn"})},"VCheckboxBtn"),B=v()({name:"VCheckboxBtn",props:C(),emits:{"update:modelValue":e=>!0,"update:indeterminate":e=>!0},setup(e,r){let{slots:s}=r;const t=c(e,"indeterminate"),n=c(e,"modelValue");function u(a){t.value&&(t.value=!1)}const i=l(()=>t.value?e.indeterminateIcon:e.falseIcon),m=l(()=>t.value?e.indeterminateIcon:e.trueIcon);return x(()=>{const a=I(o.filterProps(e),["modelValue"]);return k(o,b(a,{modelValue:n.value,"onUpdate:modelValue":[d=>n.value=d,u],class:["v-checkbox-btn",e.class],style:e.style,type:"checkbox",falseIcon:i.value,trueIcon:m.value,"aria-checked":t.value?"mixed":void 0}),s)}),{}}});export{B as V,C as m};
