"""
Comando de management para crear o actualizar el superusuario admin
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()


class Command(BaseCommand):
    help = 'Crea o actualiza el superusuario admin con contraseña admin123'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@metrolima.com'
        password = 'admin123'

        self.stdout.write('🔧 Iniciando creación/actualización de superusuario...')

        try:
            with transaction.atomic():
                # Intentar obtener el usuario existente
                try:
                    user = User.objects.get(username=username)
                    created = False
                    self.stdout.write(f'📋 Usuario "{username}" encontrado, actualizando...')
                except User.DoesNotExist:
                    # Si no existe, crear uno nuevo
                    user = User(username=username)
                    created = True
                    self.stdout.write(f'➕ Creando nuevo usuario "{username}"...')

                # Establecer todos los campos necesarios
                user.email = email
                user.is_staff = True
                user.is_superuser = True
                user.is_active = True
                user.set_password(password)
                user.save()

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'✅ Superusuario "{username}" creado exitosamente'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'✅ Superusuario "{username}" actualizado exitosamente'
                        )
                    )

                # Verificar que el usuario puede autenticarse
                user.refresh_from_db()
                if user.check_password(password):
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'✅ Verificación: La contraseña es correcta'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.ERROR(
                            f'❌ ERROR: La contraseña no coincide después de guardar'
                        )
                    )
                    raise Exception('La contraseña no se guardó correctamente')

                # Verificar permisos
                if not user.is_staff:
                    self.stdout.write(
                        self.style.WARNING(
                            f'⚠️ ADVERTENCIA: is_staff es False'
                        )
                    )
                if not user.is_superuser:
                    self.stdout.write(
                        self.style.WARNING(
                            f'⚠️ ADVERTENCIA: is_superuser es False'
                        )
                    )
                if not user.is_active:
                    self.stdout.write(
                        self.style.WARNING(
                            f'⚠️ ADVERTENCIA: is_active es False'
                        )
                    )

                # Mostrar información final
                self.stdout.write('')
                self.stdout.write(
                    self.style.SUCCESS('=' * 50)
                )
                self.stdout.write(
                    self.style.SUCCESS('✅ CREDENCIALES DEL SUPERUSUARIO:')
                )
                self.stdout.write(
                    self.style.SUCCESS(f'   Usuario: {username}')
                )
                self.stdout.write(
                    self.style.SUCCESS(f'   Contraseña: {password}')
                )
                self.stdout.write(
                    self.style.SUCCESS(f'   Email: {email}')
                )
                self.stdout.write(
                    self.style.SUCCESS('=' * 50)
                )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error al crear/actualizar superusuario: {e}')
            )
            import traceback
            self.stdout.write(self.style.ERROR(traceback.format_exc()))
            # No hacer raise para que no detenga el servidor
            # El servidor puede iniciar sin el superusuario
            self.stdout.write(
                self.style.WARNING('⚠️ Continuando con el inicio del servidor...')
            )

