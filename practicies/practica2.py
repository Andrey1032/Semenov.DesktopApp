import numpy as np
from sklearn.cluster import KMeans


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
    if not self.kmeans or self.current_step >= 10:
        return

    # Выполняем следующий шаг алгоритма
    self.kmeans.max_iter = 1
    self.kmeans.n_init = 1
    self.kmeans.fit(self.points)

    self.current_step += 1
    # Обновляем график
    print_graphic(self)


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
            ax.scatter(
                cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {label+1}')

        # Центры кластеров
        ax.scatter(centroids[:, 0], centroids[:, 1],
                    marker='X', color='black', s=100, label='Centroids')

        ax.legend(loc="best")

    self.canvas.draw()