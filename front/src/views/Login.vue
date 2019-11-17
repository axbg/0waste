<template>
  <div class="background-container">
    <div class="login-container">
      <md-card class="md-elevation-12 content-container">
        <img src="/logo.png" />
        <md-button class="md-raised md-accent big-btn" @click="login">Let's go</md-button>
      </md-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "login",
  props: ["baseUrl"],
  data: () => ({}),
  methods: {
    login: function() {
      this.$router.push({ name: "home" });
    }
  }
};
</script>

<style>
.background-container {
  background-image: url("https://images.pexels.com/photos/1533720/pexels-photo-1533720.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940");
  background-size: cover;
  height: 100%;
  width: 100%;
}
.login-container {
  margin: 0 auto;
  width: 30%;
  margin-top: 20vh;
  display: inline-block;
}
.content-container {
  padding: 20px;
}
.big-btn {
  width: 150px;
}
@media only screen and (max-width: 1200px) {
  .login-container {
    width: 90%;
  }
}
</style>