<template>
  <div class="page">
    <i class="fas fa-handshake title"></i>
    <h2 class="font-secundary">Gracias por confiar en nosotros</h2>
    <div class="msg">
      <i class="fas fa-arrow-left"></i>
      <p>A la izquierda tienes las opciones para gestionar tu cuenta</p>
    </div>
  </div>
</template>

<style scoped>
.page {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-top: 85px;
}

.page .msg {
  display: flex;
  justify-content: center;
  align-items: center;
}

.page i.title {
  font-size: 150px;
  margin: auto;
}

.page div p {
  font-size: 20px;
  margin: 0;
}

.page div i {
  font-size: 30px;
}
</style>
