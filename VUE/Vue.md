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
               































