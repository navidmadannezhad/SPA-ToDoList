<template>
    <div class="register-comp">

        <div class="content">
            <form action="">
                <input type="text" placeholder="نام کاربری..." v-model="username">
                <input type="password" placeholder="رمز عبور..." v-model="password1">
                <input type="password" placeholder="تکرار رمز عبور..." v-model="password2">
                <button class="submit" @click="register($event)">ثبت نام</button>
            </form>
        </div>

    </div>
</template>

<script>
export default {
    data: function(){
        return{
            username: '',
            password1: '',
            password2: ''
        }
    },

    methods:{
        register(event){
            event.preventDefault();
            let payload = {
                username: this.username,
                password1: this.password1,
                password2: this.password2
            };
            this.$store.dispatch('register', payload);
        }
    }
}
</script>


<style lang="scss" scoped>

@import '@/css/custom.scss';

div.register-comp{
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