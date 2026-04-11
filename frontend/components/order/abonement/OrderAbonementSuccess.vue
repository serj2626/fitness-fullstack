<script setup lang="ts">
// В реальном компоненте здесь были бы пропсы с данными
</script>

<template>
  <div class="container">
    <div class="order-abonement-success">
      <p class="order-abonement-success__title">
        Вы успешно забронировали абонемент! 🎉
      </p>
      <p class="order-abonement-success__subtitle">
        Мы свяжемся с вами в ближайшее время для подтверждения
      </p>

      <!-- Карточка с информацией -->
      <div class="order-abonement-success__card">
        <ul class="order-abonement-success__list">
          <li class="list-item">
            <div class="list-item__label">Ваше имя</div>
            <div class="list-item__value">Сергей Бойцов</div>
          </li>
          <li class="list-item">
            <div class="list-item__label">Тариф</div>
            <div class="list-item__value tariff-pro">PRO</div>
          </li>
          <li class="list-item">
            <div class="list-item__label">Дата начала</div>
            <div class="list-item__value">05-03-2025</div>
          </li>
          <li class="list-item">
            <div class="list-item__label">Статус</div>
            <div class="list-item__value status-created">
              Ожидает подтверждения
            </div>
          </li>
        </ul>
      </div>

      <!-- Действия -->
      <div class="order-abonement-success__actions">
        <BaseButton color="red" label="Отменить" :outline="true" />
        <BaseButton label="На главную" :outline="true" />
      </div>

      <!-- Дополнительная информация -->
      <div class="order-abonement-success__info">
        <p>📞 По всем вопросам звоните: <strong>+7 (999) 123-45-67</strong></p>
        <p>⏰ Часы работы: <strong>пн-вс с 7:00 до 23:00</strong></p>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.order-abonement-success {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
  padding: 40px 20px;
  background-color: $white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: visible;
}

// Стили для анимированной иконки успеха
.order-abonement-success__icon {
  margin-bottom: 10px;
}

.success-checkmark {
  width: 80px;
  height: 80px;
  margin: 0 auto;

  .check-icon {
    width: 80px;
    height: 80px;
    position: relative;
    border-radius: 50%;
    box-sizing: content-box;
    border: 4px solid #4caf50;

    &::before {
      top: 3px;
      left: -2px;
      width: 30px;
      transform-origin: 100% 50%;
    }

    &::after {
      top: 0;
      left: 30px;
      width: 60px;
      transform-origin: 0 50%;
    }

    &::before,
    &::after {
      content: "";
      height: 4px;
      background: #4caf50;
      position: absolute;
      transform: scaleX(0);
    }

    .icon-line {
      height: 4px;
      background-color: #4caf50;
      display: block;
      border-radius: 2px;
      position: absolute;
      z-index: 10;

      &.line-tip {
        top: 46px;
        left: 14px;
        width: 25px;
        transform: rotate(45deg);
        animation: icon-line-tip 0.75s;
      }

      &.line-long {
        top: 38px;
        right: 8px;
        width: 47px;
        transform: rotate(-45deg);
        animation: icon-line-long 0.75s;
      }
    }

    .icon-circle {
      top: -4px;
      left: -4px;
      z-index: 10;
      width: 80px;
      height: 80px;
      border-radius: 50%;
      border: 4px solid rgba(76, 175, 80, 0.2);
      box-sizing: content-box;
      position: absolute;
    }

    .icon-fix {
      top: 8px;
      width: 5px;
      left: 26px;
      z-index: 1;
      height: 85px;
      position: absolute;
      transform: rotate(-45deg);
    }
  }
}

@keyframes icon-line-tip {
  0% {
    width: 0;
    left: 1px;
    top: 19px;
  }
  54% {
    width: 0;
    left: 1px;
    top: 19px;
  }
  70% {
    width: 50px;
    left: -8px;
    top: 37px;
  }
  84% {
    width: 17px;
    left: 21px;
    top: 48px;
  }
  100% {
    width: 25px;
    left: 14px;
    top: 45px;
  }
}

@keyframes icon-line-long {
  0% {
    width: 0;
    right: 46px;
    top: 54px;
  }
  65% {
    width: 0;
    right: 46px;
    top: 54px;
  }
  84% {
    width: 55px;
    right: 0px;
    top: 35px;
  }
  100% {
    width: 47px;
    right: 8px;
    top: 38px;
  }
}

.order-abonement-success__title {
  text-align: center;
  font-size: clamp(1.75rem, 4vw, 2.5rem);
  font-weight: 700;
  margin: 0;
  line-height: 1.2;
}

.order-abonement-success__subtitle {
  text-align: center;
  font-size: clamp(1.1rem, 2.5vw, 1.4rem);
  color: #6b7280;
  margin: 0;
  line-height: 1.4;
  max-width: 500px;
}

.order-abonement-success__card {
  background: white;
  border-radius: 16px;
  padding: 30px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  border: 1px solid #e5e7eb;
  width: 100%;
  max-width: 500px;
}

.order-abonement-success__list {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.list-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid #f3f4f6;

  &:last-child {
    border-bottom: none;
  }

  &__label {
    font-weight: 600;
    color: #374151;
    font-size: 0.95rem;
  }

  &__value {
    font-weight: 500;
    color: #1f2937;
    font-size: 1rem;

    &.tariff-pro {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 4px 12px;
      border-radius: 20px;
      font-weight: 600;
      font-size: 0.9rem;
    }

    &.status-created {
      color: #f59e0b;
      font-weight: 600;
    }
  }
}

.order-abonement-success__actions {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  justify-content: center;

  .btn {
    padding: 12px 24px;
    border: none;
    border-radius: 12px;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
    text-align: center;
    min-width: 180px;

    &-primary {
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: white;

      &:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.3);
      }
    }

    &-secondary {
      background: white;
      color: #374151;
      border: 2px solid #d1d5db;

      &:hover {
        background: #f9fafb;
        border-color: #9ca3af;
        transform: translateY(-2px);
      }
    }
  }
}

.order-abonement-success__info {
  text-align: center;
  background: #f8f9fa;
  padding: 20px;
  border-radius: 12px;
  border-left: 4px solid #3b82f6;
  max-width: 500px;
  width: 100%;

  p {
    margin: 8px 0;
    color: #6b7280;
    font-size: 0.95rem;

    &:last-child {
      margin-bottom: 0;
    }

    strong {
      color: #374151;
    }
  }
}

// Адаптивность
@media (max-width: 768px) {
  .container {
    padding: 10px;
  }

  .order-abonement-success {
    padding: 30px 15px;
    gap: 20px;
  }

  .order-abonement-success__card {
    padding: 20px;
  }

  .order-abonement-success__actions {
    flex-direction: column;
    width: 100%;
    max-width: 300px;

    .btn {
      min-width: auto;
      width: 100%;
    }
  }

  .list-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;

    &__value {
      align-self: flex-end;
    }
  }
}

@media (max-width: 480px) {
  .success-checkmark {
    width: 60px;
    height: 60px;

    .check-icon {
      width: 60px;
      height: 60px;
    }
  }
}
</style>
