<template>
  <div class="title">
    <!-- Version movil -->
    <section class="mobile">
      <i
        v-if="history > 1"
        @click="changePage()"
        class="fas fa-arrow-circle-left back"
      ></i>
      <h2>FORGETIT</h2>
      <router-link v-if="!currentUser.username" class="user" to="/login">
        <i class="fas fa-user-circle"></i>
      </router-link>
      <router-link v-if="currentUser.username" class="user" to="/login">
        <img src="https://thispersondoesnotexist.com/image" alt="profile" />
      </router-link>
    </section>
  </div>
</template>

<script>
// Vue
import { computed } from "vue";
import { useStore } from "vuex";

export default {
  name: "TitleMobile",
  setup() {
    const store = useStore();
    const shipping = computed(() => store.state.shipping);
    const currentUser = computed(() => store.state.user.user);

    let history = window.history.length;
    console.log(history);
    return { history, shipping, currentUser };
  },
  methods: {
    changePage() {
      if (this.shipping.filters != null) {
        this.shipping.filters = null;
      } else if (this.shipping.category != null) {
        this.shipping.category = null;
      } else {
        this.$router.go(-1);
      }
    },
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
  position: fixed;
  background-color: white;
  z-index: 999;
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

.mobile .user img {
  width: 45px;
  object-fit: cover;
  margin-top: 7px;
  border-radius: 100%;
}
</style>
