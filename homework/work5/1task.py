def get_top_grade_students(all_students: dict[str, float]) -> dict[str, float]:
    top_avg_points = sorted(
        {(x, y) for (x, y) in all_students.items()},
        key=lambda item: item[1],
        reverse=True,
    )
    return dict(top_avg_points[:3])


all_students = {
    "Ivan": 456,
    "Temir": 890,
    "Andre": 156,
    "Oleg": 444,
}


assert get_top_grade_students(all_students) == {
    "Temir": 890,
    "Ivan": 456,
    "Oleg": 444,
}
print("All tests passed")
