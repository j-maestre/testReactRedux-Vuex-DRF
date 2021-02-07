<template>
  <div class="title">
    <!-- Version movil -->
    <section class="mobile">
      <i
        v-if="history > 1"
        @click="$router.go(-1)"
        class="fas fa-arrow-circle-left back"
      ></i>
      <h2>FORGETIT</h2>
      <router-link class="user" to="/login">
        <i class="fas fa-user-circle"></i>
      </router-link>
    </section>
  </div>
</template>

<script>
export default {
  name: "Header",
  setup() {
    let history = window.history.length;
    console.log(history);
    return { history };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.mobile {
  display: none;
  height: 60px;
  width: 100%;
  top: 0;
  justify-content: center;
  align-items: center;
  position: relative;
}

.mobile h2 {
  margin: 0;
  font-style: italic;
}

.mobile .user {
  position: absolute;
  right: 15px;
  font-size: 25px;
}

.mobile .back {
  position: absolute;
  left: 15px;
  font-size: 25px;
}
</style>
