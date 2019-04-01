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

# 生命周期函数

    beforeCreate(){
        // vue的data还没赋值
    }
    
    
    created(){
        // vue的data已经赋值
        // 可以在这里发ajax请求
    }
    
    
    beforeMount(){
        // 页面挂载之前    create vm.$el  and  replace el with it 
        // {{ item }} ----> xxxx
    }
    
    mounted(){
        // 页面挂载之后    
        // 可以在这里发ajax请求

    }
    
    
    
    beforeUpdate(){
        // 数据更新之前
    }
    
    updated(){
        
    }
    
    beforeDestory(){
        // 清除用到的定时器   
    }
    
    destoryed(){
    
    }
    
# Vue Router
    -   $route:  当前路由信息
        $route.params.key
        
    -   $router: 全局路由对象
    
    -   前端路由
    -   router-link
    -   router-view
    -   嵌套的路由
    -   路由的参数
    -   命名路由
    -   编程式导航
    
    
    
# 开发工具箱
    -   node.js 将Chorme的V8引擎,单独抽出来,并加入一些与系统交互、文件操作相关接口，让js可以运行在服务器上
    -   npm     包管理工具    
    -   webpack 打包工具  ,让后端开发的方式开发前段代码
    -   Vue-Cli 
    
    
# Vuex
    -   大型项目用到的状态管理器（管理跨足间的一些数据）
    
    state : 仓库，存储数据
    action: 更改store状态的唯一方法   ：提交action
        同步操作（ajax)
    mutation:   同步操作（赋值）
    module: 数据仓库，分块
    
    getter: 从store中的state中派生出一些状态
        例如：
            computed:{
                doneTodoCount(){
                    return this.$state.todos.filter(to=>todo.done).length
                }
            }
       
    
# axios    
    Vue 推荐的发送请求的工具
    
    
    
# Element-UI
    类似Bootstrap
    Vue全家桶  Vue\VueRouter\Vuex    
    
    
    