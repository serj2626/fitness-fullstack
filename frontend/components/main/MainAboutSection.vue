<script lang="ts" setup></script>
<template>
  <section id="main-about-section" class="main-about-section">
    <div class="container">
      <div class="main-about-section__text" data-aos="fade-up" data-aos-duration="2000">
        <span>СИЛА:</span>
        Тренажерный зал, кардио-зона, TRX, зона свободных весов, бассейн, бокс,
        единоборства, круговая тренировка, BUMS + ABC, PUMP, LOWER BODY, CORE+,
        табата, тай бо, body sculpt, step interval, spinning 2
        <span>РЕЛАКС:</span>
        Косметология тела и лица, гидромассаж, душ Шарко, ароматерапия,
        обертывания и пилинги, салон красоты, массаж (антицеллюлитный,
        кисточковый, скульптурирующий, баночный, медовый, стоун), этнический
        массажный кабинет, японская бочка, русская парная, джакузи, сауна, СПА,
        солярий, хамам, interval cross fitness
        <span>ЭНЕРГИЯ:</span>
        Йога, аэройога, пилатес, сайкл-студия, antiage, здоровая спина, aqua
        all, aqua mix, aqua tabata, йога для лица, йога нидра, aero yoga
      </div>
    </div>
  </section>
</template>
<style lang="scss" scoped>
.main-about-section {
  padding-block: 100px;
  background-color: $bg_block;

  &__text {
    position: relative;
    text-transform: uppercase;
    line-height: 1.5;
    font-size: 1.9rem;
    text-align-last: justify;
    color: $white;
    & span {
      color: $accent;
      &::after {
        content: " ";
        display: inline-block;
        width: 0.6em;
      }
    }
  }
}
</style>
