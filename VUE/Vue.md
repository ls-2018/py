# 原生
    -   <div id="app">
          {{ msg }}
        </div>
        
        // 引入vue.js
        var app = new Vue({
             el:'#app',
             data:{
                msg : '路飞学城'
             }
        })

 
# 指令系统
    -   v-if
        v-else-if
        v-else
    -   v-show
    # v-if  有更高的切换开销， v-show有更高的初始渲染开销。--->需要频繁的切换使用v-if,否则使用v-show
    
    -   v-bind  :   绑定属性
    -   v-on    @   绑定事件
    -   v-for   
    -   v-html
    -   v-text
    
    -   v-model # 只适用在表单控件中
        v-model="currentItem"