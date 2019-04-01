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
        
        
# 局部组件
# 全局组件
    -   Vue.component(
            '组件名',
            {
                template:'',
                    data(){
                    return{}
                }
            }
        )

# 父组件->子组件传值
    父组件     v-on:name='xxxxx'
    子组件     props:['name']


# 子组件->父组件传值
    子组件抛出自定义事件  this.$emit('事件名','数据')     
    父组件监听自定义事件  v-on:事件名=函数

# 非父子组件间传值
    借助中间对象
        var bus = new Vue()
    组件1：
        bus.$emit('事件名'，'数据')
    组件2：
        bus.$on('事件名')
        