import { setYear, isAfter } from 'date-fns'

export function getNextBirthday(birthday: Date): Date {
  const thisYear = setYear(birthday, new Date().getFullYear())
  if (isAfter(thisYear, new Date())) {
    return thisYear
  }
  const nextYear = setYear(birthday, new Date().getFullYear() + 1)
  return nextYear
}
