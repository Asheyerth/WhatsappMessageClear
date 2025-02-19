<template>
<h2>
    Ingresar mensaje
</h2>
<form>
    <textarea v-model="userInput.message" placeholder="Ingrese su mensaje"/>
    <input type="text" v-model="userInput.userSender">
    <input type="text" v-model="userInput.userReplace">
    <button v-on:click.prevent=clearBasicMessage>Basic Clean</button>
    <button v-on:click.prevent=clearUserMessage>User Sender Clean</button>
    <button v-on:click.prevent=clearReplaceMessage>User Replace Clean</button>
</form>
{{ userInput }}
{{ userInput.message }}

</template>

<script>
//<input type="text" v-model="userInput.message">
//import axios from 'axios';
//import api from './plugins/axios.js';
export default {
  name: 'PostRequestClearMessage',
  data(){
    return {
      userInput: {
        message: 'mensaje',
        userSender: 'usuario enviador',
        userReplace: 'usuario reemplazo'
      }
    }
  },
  methods: {
    async clearBasicMessage() {
      try {
        console.log('Enviando')
        const response = await this.$axios.post('/BasicClean', {
          // Datos que deseas enviar
          input: this.userInput
        });
        console.log('Enviado y revisado')
        console.log(response.data); // La respuesta del servidor
      } catch (error) {
        console.error('Error al enviar la solicitud:', error);
      }
    },
    //Otro endpoint 
    //async deleteMessage() {asdasdas}
    async clearUserMessage() {
      try {
        console.log('Enviando')
        const response = await this.$axios.post('/UserClean', {
          // Datos que deseas enviar
          input: this.userInput
        });
        console.log('Enviado y revisado')
        console.log(response.data); // La respuesta del servidor
      } catch (error) {
        console.error('Error al enviar la solicitud:', error);
      }
    },
    async clearReplaceMessage() {
      try {
        console.log('Enviando')
        const response = await this.$axios.post('/UserReplaceClean', {
          // Datos que deseas enviar
          input: this.userInput
        });
        console.log('Enviado y revisado')
        console.log(response.data); // La respuesta del servidor
      } catch (error) {
        console.error('Error al enviar la solicitud:', error);
      }
    }
  }
}




//export default {
//  name: 'InputMessage',
//  methods: {
//    clearMessage(){
        //Envio a backend
        //axios

//    }
//  },
//  data(){
//    return {
//        userInput: ""
//    }
//  }
  //props: {
    //msg: String
  //}
//}
</script>