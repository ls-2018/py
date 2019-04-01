# Es6
    -   变量提升:(同一个作用域内）
        -   function f1(){
                console.log(s1);
                var s1 = 123;
            }
            -------> undefined
            相当于
            
            function f1(){
                var s1;
                console.log(s1);
                s1 = 123;
                
            }
        
        
        -   function f1(){
                console.log(s1);
                if (false){
                    var s1 = 123;   # 相当于写在外面，Es5里没有块级作用域的,var写在里面和外面没区别
                }
            }
            
        -   function f1(){
                console.log(s1);
                if (false){
                    let s1 = 123;   # Es6里有块级作用域的
                }
            }   
    -   模板字符串   
        `${}`    
        
        -   python3.6之后
            -   字典默认会记录添加顺序
            -   类型注解
                def foo(n1: int,n2: int)->int:
                    
            -   name = 'alex'
                print(f'{name} dsb.')
               
    -   对象简洁法
        - {'x':x, 'y':y}
        - {x:x, y:y}
        - {x,y}

    -   深浅拷贝
        
        var z = Object.assign({},x) # 深拷贝


    -   给父类绑定方法
        String.prototype.dsb=function(){
            console.log('xxx')
        }

    -   
        class Point{
            constructor(x,y){
                this.x=x;
                this.y=y;
            } // 不加逗号
            toString(){
                return `(${this.x},${this.y}`
            }
         
        var p = new Point(10,20)
        console.log(p.x)
        p.toString();
        
        
        class ColorPoint extends Point{
            constructor(x,y,color){
                super(x,y); // 调用父类的constructor(x,y)
                this.color=color;
            } // 不加逗号
            toString(){
                return `(${this.x},${this.y}`
            }
         
        var p = new Point(10,20)
        console.log(p.x)
        p.toString();


    -   箭头函数
        （）->{
            this指向父级对象
        }










