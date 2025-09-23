export interface IReview {
  id: string;
  first_name: string; // Имя автора отзыва
  last_name: string;
  email: string; // Email автора
  rating: number; // Оценка (1-5)
  text: string; // Текст отзыва
  verified: boolean; // Подтвержденный отзыв
  time_age: string; // Время создания (лучше использовать Date или string в ISO формате)
}

