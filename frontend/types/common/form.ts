export interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}