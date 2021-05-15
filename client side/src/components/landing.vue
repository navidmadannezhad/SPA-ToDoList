<template>
  <div class="landing-comp">

    <div class="content">
      <h1 class="title">برنامه روزانه</h1>
      <p class="introduction">برنامه روزانت رو اینجا بنویس</p>
      <router-link tag="button" to="/auth">شروع کنیم</router-link>
    </div>
    
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>

div.landing-comp{
  width: 100%;
  height: 100%;
  background: #141E30; 
  background: -webkit-linear-gradient(to left, #243B55, #141E30);
  background: linear-gradient(to left, #243B55, #141E30);
  display: flex;
  justify-content: center;
  align-items: center;

  div.content{
    width: 80%;
    display: flex;
    flex-direction: column;
    align-items: center;
    & > *{
      margin-bottom: 30px;
      text-shadow: 0px 4px 4px rgba(0,0,0,0.5);
    }
    h1.title{
      font-size: 3.2rem;
      font-weight: bold;
    }
    p.introduction{
      font-size: 1.2rem;
      opacity: 0.4;
    }
    button{
      padding: 15px 70px;
      border: none;
      background-color: #45b884;
      border-radius: 50px;
      font-family: iransansweb;
      text-shadow: none;
      box-shadow: 0px 4px 4px rgba(0,0,0,0.5);
    }
  }
}
</style>
