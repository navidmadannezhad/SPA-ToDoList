<template>
    <div class="login-comp">

        <message-component></message-component>

        <div class="content">
            <form action="">
                <input type="text" placeholder="نام کاربری...">
                <input type="password" placeholder="رمز عبور...">
                <router-link to="/panel" tag="button" class="submit">ورود</router-link>
            </form>
        </div>

    </div>
</template>

<script>
import messageComponent from '../message.vue';
export default {
    components:{
        'message-component': messageComponent
    }
}
</script>


<style lang="scss" scoped>

@import '@/css/custom.scss';

div.login-comp{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;

    div.content{
        width: 100%;
        form{
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            & > *{
                margin-bottom: 30px;
            }
            input, button.submit{
                @include input();
            }
            button.submit{
                @include button();
            }
        }
    }
}
</style>