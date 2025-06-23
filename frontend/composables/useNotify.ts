type NotificationType = 'success' | 'error' | 'warning' | 'info'

interface Notification {
  id: number
  type: NotificationType
  message: string
  timeout?: number
}

export default function useNotify() {
  const notifications = useState<Notification[]>('notifications', () => [])

  const removeNotification = (id: number) => {
    notifications.value = notifications.value.filter(n => n.id !== id)
  }

  const addNotification = (type: NotificationType, message: string, timeout = 3000) => {
    const id = Date.now()
    notifications.value.push({ id, type, message, timeout })

    if (timeout > 0) {
      setTimeout(() => removeNotification(id), timeout)
    }
  }

  return {
    success: (msg: string, timeout?: number) => addNotification('success', msg, timeout),
    error: (msg: string, timeout?: number) => addNotification('error', msg, timeout),
    warning: (msg: string, timeout?: number) => addNotification('warning', msg, timeout),
    info: (msg: string, timeout?: number) => addNotification('info', msg, timeout),
    notifications,
    removeNotification,
  }
}