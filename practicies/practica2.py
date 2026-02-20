import numpy as np
from sklearn.cluster import KMeans
from PySide6.QtWidgets import QMessageBox
from scipy.spatial.distance import euclidean


def run_algorithm(self):
    num_points = self.num_points_spin.value()
    num_clusters = self.num_clusters_spin.value()

    # Генерация случайных точек
    points = np.random.rand(num_points, 2)

    # Запуск K-means
    kmeans = KMeans(n_clusters=num_clusters, max_iter=1, init='random')
    kmeans.fit(points)

    # Сохраняем состояние в главном окне
    self.points = points
    self.kmeans = kmeans
    self.current_step = 0

    # Обновляем график
    print_graphic(self)


def step_algorithm(self):
    if not self.kmeans:
        return

    # Сохраняем предыдущие центры перед началом следующего шага
    previous_centroids = self.kmeans.cluster_centers_.copy()

    # Выполняем следующий шаг алгоритма
    self.kmeans.max_iter = 1
    self.kmeans.n_init = 1
    self.kmeans.fit(self.points)

    # Получаем новую конфигурацию центров
    current_centroids = self.kmeans.cluster_centers_

    # Определяем разницу между старыми и новыми центрами
    total_diff = sum(euclidean(prev_cen, curr_cen) for prev_cen, curr_cen in zip(previous_centroids, current_centroids))

    # Если разница мала (< 0.1), считаем алгоритм завершённым
    if total_diff < 0.1:
        final_results(self)
        return

    # Иначе увеличиваем счётчик шагов
    self.current_step += 1

    # Обновляем график
    print_graphic(self)


def final_results(self):
    # Получаем последнюю конфигурацию центров и меток
    labels = self.kmeans.labels_
    centroids = self.kmeans.cluster_centers_

    # Начинаем формировать таблицу
    html_table = """
    <html><head></head><body style="font-family:Arial">
      <h2 align="center">Итоговая таблица кластеров</h2>
      <table border="1" cellpadding="5" cellspacing="0" width="100%">
          <tr bgcolor="#dddddd"><th>Номер кластера</th><th>Координата x</th><th>Координата y</th><th>Первые 5 точек</th></tr>
    """

    # Генерируем строки таблицы
    for i, centroid in enumerate(centroids):
        cluster_points = self.points[labels == i]
        first_five_points = ', '.join([f"({p[0]:.3f}, {p[1]:.3f})" for p in cluster_points[:5]])
        remaining_points = "" if len(cluster_points) <= 5 else f"... и ещё {len(cluster_points)-5}"

        row_html = f"""
           <tr>
               <td>{i}</td>
               <td>{centroid[0]:.3f}</td>
               <td>{centroid[1]:.3f}</td>
               <td>{first_five_points}{remaining_points}</td>
           </tr>
        """
        html_table += row_html

    # Завершение формирования таблицы
    html_table += "</table>"

    # Полное сообщение
    full_message = f"""\
    <html><head></head><body style="font-family:Arial">
       <h1 align="center">Алгоритм завершён</h1>
       <p>Всего выполнено шагов: {self.current_step}<br/>
       Количество кластеров: {len(centroids)}
       </p>
       {html_table}
    </body></html>
    """

    # Показываем итоговое сообщение
    QMessageBox.information(self, 'Итоговый результат', full_message)


def reset(self):
    self.points = None
    self.clusters = None
    self.kmeans = None
    self.current_step = 0
    # Обновляем график
    print_graphic(self)

def print_graphic(self):
    ax = self.fig.clear()
    ax = self.fig.add_subplot(111)

    if self.points is not None and self.kmeans is not None:
        labels = self.kmeans.labels_
        centroids = self.kmeans.cluster_centers_

        # Рисуем точки
        for label in range(len(centroids)):
            cluster_points = self.points[labels == label]
            ax.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {label+1}')

        # Центры кластеров
        ax.scatter(centroids[:, 0], centroids[:, 1], marker='X', color='black', s=100, label='Centroids')

        ax.legend(loc="best")

    self.canvas.draw()