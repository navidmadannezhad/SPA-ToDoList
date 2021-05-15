<template>
    <div class="auth-comp">

        <div class="content">
            
            <div class="auth-buttons">
                <router-link to="/auth/login" tag="button" class="login">ورود</router-link>
                <router-link to="/auth/register" tag="button" class="register">ثبت نام</router-link>
            </div>

            <div class="auth-panel">
                <router-view>
                </router-view>
            </div>
            
        </div>

    </div>
</template>


<script>
export default {
    mounted(){
        this.$router.push('/auth/register');
    }
}
</script>


<style lang="scss" scoped>

@import '@/css/custom.scss';

div.auth-comp{
  width: 100%;
  height: 100%;
  background: #141E30; 
  background: -webkit-linear-gradient(to left, #243B55, #141E30);
  background: linear-gradient(to left, #243B55, #141E30);
  display: flex;
  justify-content: center;

  div.content{
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 70%;
      margin-top: 20vh;

      div.auth-buttons{
          width: 100%;
          display: flex;
          justify-content: space-between;
          button{
              @include button();
              width: 50%;
              background-color: rgba(93, 131, 168, 0.4);
              &.login{
                  border-top-left-radius: 0;
                  border-bottom-left-radius: 0;
              }
              &.register{
                  border-top-right-radius: 0;
                  border-bottom-right-radius: 0;
              }
              &.router-link-exact-active{
                  background-color: #45b884;
              }
          }
      }

      div.auth-panel{
          width: 100%;
          margin-top: 8vh;  
      }
  }
}
</style>