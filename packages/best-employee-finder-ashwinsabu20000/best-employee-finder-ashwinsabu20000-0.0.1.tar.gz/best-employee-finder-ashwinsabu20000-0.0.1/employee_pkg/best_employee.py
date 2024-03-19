class BestEmployee:

    def __init__(self):
        self.employee = []

    def add_employee(self, name, total_hours, rating, orders_taken):
        self.employee.append({
            'name': name,
            'total_hours': total_hours,
            'rating': rating,
            'orders_taken': orders_taken
        })

    def evaluate(self):
        scores = [] # To append the scores of all the employees
        for employee in self.employee:
            score = employee['total_hours'] * 0.1 + employee['rating'] * 0.6 + employee['orders_taken'] * 0.7
            scores.append((employee['name'], score))

        ranking = sorted(scores, key=lambda x: x[1], reverse=True)

        # Get the best employee
        best_emp = ranking[0][0]

        return {
            'ranking': ranking,
            'best_emp': best_emp
        }