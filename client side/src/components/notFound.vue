<template>
    <div class="notfound-comp" ref="notfoundComp">
        
        <div class="intro">

            <div class="main">
                <p class="message">Not Found</p>
                <p class="number">404</p>
            </div>

            <p class="sub">صفحه مورد نظر شما پیدا نشد</p>

            <a @click="goBack()">
                بازگشت
            </a>

        </div>

    </div>
</template>

<script>
export default {
    methods:{
        goBack(){
            this.$router.go(-1);
        }
    }
}
</script>

<style lang="scss" scoped>
div.notfound-comp{
    width: 100%;
    min-height: 100vh;
    background: #141E30; 
    background: -webkit-linear-gradient(to left, #243B55, #141E30);
    background: linear-gradient(to left, #243B55, #141E30);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family: iransansweb;
    div.intro{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        div.main{
            display: flex;
            width: 220px;
            justify-content: space-between;
            align-items: center;
            p{
                color: white;
                &:nth-child(2){
                    font-size: 4rem;
                }
            }
        }
        p.sub{
            color: white;
        }
        a{
            display: inline-block;
            background-color: #45b884;
            border-radius: 15px;
            padding: 10px 30px;
            color: white;
            margin-top: 20px;
        }
    }
}

</style>