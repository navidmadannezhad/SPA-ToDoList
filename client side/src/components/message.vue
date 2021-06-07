<template>
    <div class="msg-comp">

        <div class="messages" ref="messages">
            <p class="message" v-bind:class="[ message.success ? 'success' : '', 'failure' ]" v-for="message in messages" v-bind:key="message.content">
                {{ message.content }}
            </p>
        </div>

    </div>
</template>


<script>
export default {
    props: [
        'serverMessagesBox',
        'serverMessageState'
    ],
    data: function(){
        return{
            messages: []
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
            }, 5000);
        },

        hideMessages(){
            let messages = this.$refs.messages.childNodes;
            
            Object.keys(messages).reverse().forEach((index) => {
                setTimeout(()=>{
                    setTimeout(()=>{
                        messages[index].style.right = '-1000%';
                    },250)
                        messages[index].style.right = '10%';
                }, index*100);
            });
        },

        // This function turns the server django message into client message, to render it more easily
        // boxState shows wheater the message has came from the THEN block or the CATCH block, which means the success or failure of the operation
        serverMessageOrganizer(serverMessagesBox, boxState){
            let clientMessagesBox = []
            // --

            Object.keys(serverMessagesBox).forEach(serverMessage => {
                let clientMessage = {
                    content: '',
                    success: boxState ? true : false
                }

                clientMessage.content = serverMessagesBox[serverMessage][0]
                clientMessagesBox.push(clientMessage)
            })

            // --
            return clientMessagesBox;
        }
    },

    watch:{
        serverMessagesBox(){
            this.messages = this.serverMessageOrganizer(this.serverMessagesBox, this.serverMessageState)
            setTimeout(()=>{
                this.showMessages();
            }, 1000);
        }
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