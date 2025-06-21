// ~/assets/data/visits.data.ts
export interface Visit {
  id: number;
  date: string;
  time: string;
  coach: string;
  activity: string;
  status: 'completed' | 'upcoming' | 'cancelled';
  duration: number; // в минутах
  calories?: number;
  notes?: string;
}

export const mockVisits: Visit[] = [
  {
    id: 1,
    date: '2023-10-15',
    time: '18:00',
    coach: 'Анна Иванова',
    activity: 'Функциональный тренинг',
    status: 'completed',
    duration: 60,
    calories: 450,
    notes: 'Отличная тренировка!'
  },
  {
    id: 2,
    date: '2023-10-17',
    time: '09:30',
    coach: 'Иван Петров',
    activity: 'Йога',
    status: 'upcoming',
    duration: 45
  },
  {
    id: 3,
    date: '2023-10-10',
    time: '19:00',
    coach: 'Мария Сидорова',
    activity: 'Персональная тренировка',
    status: 'cancelled',
    duration: 60
  }
];