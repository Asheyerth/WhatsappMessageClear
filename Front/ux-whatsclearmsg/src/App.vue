<template>
  <img alt="Vue logo" src="./assets/Muffin.webp">
  <ProfileTemplate msg="Welcome to Your Cleaning Whatsapp Msg app"/>
  <InputMessage></InputMessage>
  <OutputMessage></OutputMessage>
</template>

<script>
import ProfileTemplate from './components/ProfileTemplate.vue'
import InputMessage from './components/Input.vue';
import OutputMessage from './components/Output.vue';

export default {
  name: 'App',
  components: {
    ProfileTemplate,
    InputMessage,
    OutputMessage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
