<template>
    <div class="msg-comp">

        <div class="messages" v-if="messages.length != 0" ref="messages">
            <p class="message" v-bind:class="[ message.success ? 'success' : '', 'failure' ]" v-for="message in messages" v-bind:key="message.content">
                {{ message.content }}
            </p>
        </div>

    </div>
</template>


<script>
export default {
    data: function(){
        return{
            messages: [
                {
                    content: 'لطفا پسوورد را وارد کنید',
                    success: false 
                },
                {
                    content: 'لطفا نام کاربرری را وارد کنید',
                    success: false 
                },
                {
                    content: 'ورود با موفقیت انجام شد',
                    success: true 
                },
            ]
        }
    },

    methods:{
        showMessages(){
            let messages = this.$refs.messages.childNodes;

            messages.forEach((message, index) => {
                setTimeout(()=>{
                    setTimeout(()=>{
                        message.style.right = '0%';
                    },250)
                    message.style.right = '10%';
                }, index*100);
            });

            setTimeout(()=>{
                this.hideMessages();
            }, 2000);
        },

        hideMessages(){
            let messages = this.$refs.messages.childNodes;
            
            Object.keys(messages).reverse().forEach((index) => {
                setTimeout(()=>{
                    setTimeout(()=>{
                        messages[index].style.right = '-1000px';
                    },250)
                        messages[index].style.right = '10%';
                }, index*100);
            });
        }
    },

    mounted(){
        setTimeout(()=>{
            this.showMessages();
        }, 1000);
    }
}
</script>


<style lang="scss" scoped>
div.msg-comp{
    position: absolute;
    top: 0;
    left: 0px;
    width: 100%;
    display: flex;
    justify-content: center;
    div.messages{
        width: 70%;
        p.message{
            padding: 5px;
            font-size: 0.8rem;
            border-radius: 10px;
            margin-top: 10px;
            position: relative;
            right: -1000px;

            // neccessary for the translation proccess
            transition: all 0.25s;
        }
    }

    .success{
        background-color: #45b884 !important;
    }
    .failure{
        background-color: #ff2e2e;
    }
}

/* -- Messages animations -- */

</style>